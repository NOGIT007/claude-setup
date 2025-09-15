#!/usr/bin/env python3
"""
Claude Setup Manager - TUI for managing Claude Code configurations
Optimizes token usage by selectively loading components.
"""
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field

import click
from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.widgets import (
    Button, Checkbox, Footer, Header, Label,
    Static, Input, RadioSet, RadioButton, Tree
)
from textual.binding import Binding


@dataclass
class Component:
    name: str
    category: str
    description: str
    token_usage: int
    file_path: Path
    content: str = ""

    def __post_init__(self):
        if self.file_path.exists():
            self.content = self.file_path.read_text()


@dataclass
class MCPServer:
    name: str
    description: str
    token_usage: int
    tools_count: int
    category: str
    use_cases: List[str]
    when_to_load: List[str]

    @classmethod
    def from_config(cls, config_path: Path) -> "MCPServer":
        config = json.loads(config_path.read_text())
        return cls(**config)


@dataclass
class ProjectConfig:
    project_path: Path
    existing_claude_md: Optional[Path] = None
    is_existing: bool = False
    selected_agents: Set[str] = field(default_factory=set)
    selected_commands: Set[str] = field(default_factory=set)
    selected_output_styles: Set[str] = field(default_factory=set)
    selected_mcp_servers: Set[str] = field(default_factory=set)

    @property
    def total_tokens(self) -> int:
        """Calculate total estimated token usage"""
        total = 0
        # MCP servers contribute most tokens
        claude_setup = Path.home() / "code" / "claude-setup"
        for server_name in self.selected_mcp_servers:
            config_path = claude_setup / "mcp-servers" / server_name / "config.json"
            if config_path.exists():
                config = json.loads(config_path.read_text())
                total += config.get("token_usage", 0)

        # Components contribute minimal tokens
        total += len(self.selected_agents) * 200
        total += len(self.selected_commands) * 150
        total += len(self.selected_output_styles) * 100

        return total


class ComponentSelector(Static):
    """Widget for selecting components with checkboxes"""

    def __init__(self, title: str, components: List[Component], selected: Set[str]):
        super().__init__()
        self.title = title
        self.components = components
        self.selected = selected
        self.checkboxes: List[Checkbox] = []

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label(f"[bold]{self.title}[/bold]", classes="section-title")
            for component in self.components:
                # Create valid ID by replacing invalid characters
                title_clean = self.title.lower().replace(' ', '_').replace('-', '_')
                name_clean = component.name.replace('-', '_').replace(' ', '_')
                checkbox = Checkbox(
                    f"{component.name} - {component.description[:50]}...",
                    value=component.name in self.selected,
                    id=f"{title_clean}_{name_clean}"
                )
                self.checkboxes.append(checkbox)
                yield checkbox

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        """Handle checkbox state changes"""
        # Extract component name from ID (format: category_componentname)
        parts = event.checkbox.id.split("_", 1)
        if len(parts) > 1:
            component_name = parts[1].replace("_", "-")
        else:
            component_name = parts[0].replace("_", "-")
        if event.value:
            self.selected.add(component_name)
        else:
            self.selected.discard(component_name)

        # Update parent app's token calculation
        self.app.update_token_display()


class MCPServerSelector(Static):
    """Widget for selecting MCP servers with token display"""

    def __init__(self, servers: List[MCPServer], selected: Set[str]):
        super().__init__()
        self.servers = servers
        self.selected = selected
        self.checkboxes: List[Checkbox] = []

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("[bold]MCP Servers[/bold]", classes="section-title")
            for server in self.servers:
                tokens_kb = server.token_usage / 1000
                # Create valid ID for MCP server
                server_name_clean = server.name.replace('-', '_').replace(' ', '_')
                checkbox = Checkbox(
                    f"{server.name} ({tokens_kb:.1f}k tokens) - {server.description[:40]}...",
                    value=server.name in self.selected,
                    id=f"mcp_{server_name_clean}"
                )
                self.checkboxes.append(checkbox)
                yield checkbox

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        """Handle MCP server selection changes"""
        # Extract server name from ID (format: mcp_servername)
        parts = event.checkbox.id.split("_", 1)
        if len(parts) > 1:
            server_name = parts[1].replace("_", "-")
        else:
            server_name = parts[0].replace("_", "-")
        if event.value:
            self.selected.add(server_name)
        else:
            self.selected.discard(server_name)

        # Update parent app's token calculation
        self.app.update_token_display()


class TokenDisplay(Static):
    """Widget showing current token usage estimate"""

    def __init__(self, config: ProjectConfig):
        super().__init__()
        self.config = config

    def compose(self) -> ComposeResult:
        yield Label(self.get_token_text(), id="token-display")

    def get_token_text(self) -> str:
        total = self.config.total_tokens
        percentage = (total / 200000) * 100  # Assuming 200k context window
        color = "green" if percentage < 5 else "yellow" if percentage < 10 else "red"
        return f"[{color}]Token Usage: {total:,} (~{percentage:.1f}%)[/{color}]"

    def update_display(self):
        """Update the token display"""
        self.query_one("#token-display", Label).update(self.get_token_text())


class ClaudeManagerApp(App):
    """Main TUI application"""

    CSS = """
    .section-title {
        text-style: bold;
        color: #66d9ff;
        margin: 0 0 1 0;
        background: transparent;
        padding: 0 1;
    }

    #token-display {
        text-align: center;
        margin: 0 1 1 1;
        padding: 1;
        border: solid #00ff88;
        background: #1a1a1a;
        color: #00ff88;
    }

    #project-info {
        margin: 0 1 1 1;
        padding: 1;
        border: solid #ffaa00;
        background: #1a1a1a;
        color: #ffaa00;
    }

    .left-column {
        width: 50%;
        padding: 0 1;
    }

    .right-column {
        width: 50%;
        padding: 0 1;
    }

    .button-row {
        height: 3;
        margin: 1;
        align: center middle;
    }

    Checkbox {
        margin: 0;
        padding: 0 1;
        background: transparent;
        color: #ffffff;
    }

    Checkbox:focus {
        background: #333333;
        color: #66d9ff;
    }

    Checkbox.-checked {
        color: #00ff88;
    }

    Button {
        margin: 0 1;
    }

    Button.-primary {
        background: #00ff88;
        color: #000000;
    }

    ComponentSelector {
        height: auto;
        max-height: 20;
        margin: 0 0 1 0;
        border: solid #444444;
        background: #1a1a1a;
    }

    MCPServerSelector {
        height: auto;
        max-height: 20;
        margin: 0 0 1 0;
        border: solid #444444;
        background: #1a1a1a;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("g", "generate", "Generate"),
        Binding("s", "sync", "Sync"),
        Binding("u", "upload", "Upload"),
        Binding("d", "download", "Download"),
        Binding("up", "cursor_up", "Up", show=False),
        Binding("down", "cursor_down", "Down", show=False),
        Binding("space", "toggle_selection", "Toggle", show=False),
    ]

    def __init__(self):
        super().__init__()
        self.claude_setup_path = Path.home() / "code" / "claude-setup"
        self.project_config = self.detect_project()
        self.components = self.load_components()
        self.mcp_servers = self.load_mcp_servers()

    def detect_project(self) -> ProjectConfig:
        """Detect current project and existing configuration"""
        current_dir = Path.cwd()
        claude_dir = current_dir / ".claude"
        claude_md = claude_dir / "CLAUDE.md"

        config = ProjectConfig(
            project_path=current_dir,
            existing_claude_md=claude_md if claude_md.exists() else None,
            is_existing=claude_md.exists()
        )

        if config.is_existing:
            # Parse existing CLAUDE.md to pre-select components
            self.parse_existing_config(config)

        return config

    def parse_existing_config(self, config: ProjectConfig):
        """Parse existing CLAUDE.md to determine current selections"""
        if not config.existing_claude_md:
            return

        content = config.existing_claude_md.read_text()

        # Simple parsing - look for component mentions
        # This could be enhanced with proper markdown parsing
        if "code-reviewer" in content:
            config.selected_agents.add("code-reviewer")
        if "test-runner" in content:
            config.selected_agents.add("test-runner")
        # Add more parsing logic as needed

    def load_components(self) -> Dict[str, List[Component]]:
        """Load all available components"""
        components = {
            "agents": [],
            "commands": [],
            "output-styles": []
        }

        for category in components.keys():
            category_path = self.claude_setup_path / category
            if category_path.exists():
                for file_path in category_path.glob("*.md"):
                    components[category].append(Component(
                        name=file_path.stem,
                        category=category,
                        description=f"{category.title()} component",
                        token_usage=200,  # Estimated
                        file_path=file_path
                    ))

        return components

    def load_mcp_servers(self) -> List[MCPServer]:
        """Load available MCP servers"""
        servers = []
        mcp_path = self.claude_setup_path / "mcp-servers"

        if mcp_path.exists():
            for server_dir in mcp_path.iterdir():
                if server_dir.is_dir():
                    config_path = server_dir / "config.json"
                    if config_path.exists():
                        try:
                            servers.append(MCPServer.from_config(config_path))
                        except Exception as e:
                            print(f"Error loading {server_dir.name}: {e}")

        return servers

    def compose(self) -> ComposeResult:
        """Build the UI"""
        yield Header()

        # Top info section
        project_name = self.project_config.project_path.name
        status = "Existing" if self.project_config.is_existing else "New"
        yield Static(f"Project: {project_name} ({status})", id="project-info")
        yield TokenDisplay(self.project_config)

        # Main content in horizontal layout
        with Horizontal():
            # Left column - Components
            with Vertical(classes="left-column"):
                yield ComponentSelector(
                    "Agents",
                    self.components.get("agents", []),
                    self.project_config.selected_agents
                )
                yield ComponentSelector(
                    "Commands",
                    self.components.get("commands", []),
                    self.project_config.selected_commands
                )

            # Right column - Styles and MCP
            with Vertical(classes="right-column"):
                yield ComponentSelector(
                    "Output Styles",
                    self.components.get("output-styles", []),
                    self.project_config.selected_output_styles
                )
                yield MCPServerSelector(
                    self.mcp_servers,
                    self.project_config.selected_mcp_servers
                )

        # Bottom action buttons
        with Horizontal(classes="button-row"):
            yield Button("Generate", id="generate-btn", variant="primary")
            yield Button("Sync", id="sync-btn")
            yield Button("Upload", id="upload-btn")
            yield Button("Download", id="download-btn")

        yield Footer()

    def update_token_display(self):
        """Update the token usage display"""
        token_widget = self.query_one(TokenDisplay)
        token_widget.update_display()

    def action_generate(self):
        """Generate CLAUDE.md file"""
        claude_md_content = self.generate_claude_md()

        # Ensure .claude directory exists
        claude_dir = self.project_config.project_path / ".claude"
        claude_dir.mkdir(exist_ok=True)

        claude_md_path = claude_dir / "CLAUDE.md"

        # Create backup if file exists
        if claude_md_path.exists():
            self.create_backup(claude_md_path)

        # Write CLAUDE.md
        claude_md_path.write_text(claude_md_content)

        self.notify(f"Generated {claude_md_path}")
        self.exit()

    def create_backup(self, claude_md_path: Path):
        """Create backup of existing CLAUDE.md"""
        backup_dir = claude_md_path.parent / "history"
        backup_dir.mkdir(exist_ok=True)

        # Create timestamped backup
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = backup_dir / f"CLAUDE_{timestamp}.md"

        # Copy current file to backup
        import shutil
        shutil.copy2(claude_md_path, backup_path)

        # Clean old backups (keep last 10)
        backups = sorted(backup_dir.glob("CLAUDE_*.md"))
        if len(backups) > 10:
            for old_backup in backups[:-10]:
                old_backup.unlink()

        self.notify(f"Backup created: {backup_path.name}")

    def generate_claude_md(self) -> str:
        """Generate the CLAUDE.md content based on selections"""
        lines = [
            "# Project Configuration",
            "## Token Optimization",
            f"Estimated usage: {self.project_config.total_tokens:,} tokens (~{(self.project_config.total_tokens/200000)*100:.1f}%)",
            "",
            "## MCP Servers",
            "Load only when needed:"
        ]

        if self.project_config.selected_mcp_servers:
            for server_name in self.project_config.selected_mcp_servers:
                server = next((s for s in self.mcp_servers if s.name == server_name), None)
                if server:
                    lines.append(f"- {server_name}: {server.description}")
                    lines.append(f"  Load when: {', '.join(server.when_to_load[:3])}")
        else:
            lines.append("- None selected (0% MCP tokens)")

        lines.extend(["", "## Active Components"])

        if self.project_config.selected_agents:
            lines.append("### Agents")
            for agent in self.project_config.selected_agents:
                lines.append(f"- {agent}")

        if self.project_config.selected_commands:
            lines.append("### Commands")
            for command in self.project_config.selected_commands:
                lines.append(f"- {command}")

        if self.project_config.selected_output_styles:
            lines.append("### Output Style")
            for style in self.project_config.selected_output_styles:
                lines.append(f"- {style}")

        lines.extend([
            "",
            "## Instructions",
            "This configuration keeps initial token usage minimal.",
            "Load MCP servers on-demand during your session by saying:",
            "- 'load github mcp' when ready to commit",
            "- 'load playwright' for testing",
            "- 'load neo4j' for database work"
        ])

        return "\n".join(lines)

    def action_sync(self):
        """Sync with GitHub"""
        self.notify("Syncing with GitHub...")
        # TODO: Implement GitHub sync

    def action_upload(self):
        """Upload to GitHub"""
        self.notify("Uploading to GitHub...")
        # TODO: Implement GitHub upload

    def action_download(self):
        """Download from GitHub"""
        self.notify("Downloading from GitHub...")
        # TODO: Implement GitHub download

    def action_quit(self):
        """Quit the application"""
        self.exit()

    def action_cursor_up(self):
        """Move focus up"""
        self.focus_previous()

    def action_cursor_down(self):
        """Move focus down"""
        self.focus_next()

    def action_toggle_selection(self):
        """Toggle the currently focused checkbox"""
        focused = self.focused
        if isinstance(focused, Checkbox):
            focused.toggle()

    @on(Button.Pressed, "#generate-btn")
    def handle_generate_button(self):
        self.action_generate()

    @on(Button.Pressed, "#sync-btn")
    def handle_sync_button(self):
        self.action_sync()

    @on(Button.Pressed, "#upload-btn")
    def handle_upload_button(self):
        self.action_upload()

    @on(Button.Pressed, "#download-btn")
    def handle_download_button(self):
        self.action_download()


@click.command()
@click.option('--project', '-p', help='Project directory path')
def main(project: Optional[str]):
    """Claude Setup Manager - Optimize Claude Code token usage"""

    if project:
        project_path = Path(project).expanduser().resolve()
        if not project_path.exists():
            click.echo(f"Project path {project_path} does not exist")
            return
        os.chdir(project_path)

    # Check if claude-setup exists
    claude_setup = Path.home() / "code" / "claude-setup"
    if not claude_setup.exists():
        click.echo("claude-setup directory not found at ~/code/claude-setup")
        click.echo("Please clone the repository first:")
        click.echo("  git clone https://github.com/NOGIT007/claude-setup ~/code/claude-setup")
        return

    app = ClaudeManagerApp()
    app.run()


if __name__ == "__main__":
    main()