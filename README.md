# Claude Setup Manager

A TUI tool to manage Claude Code configurations and reduce token usage by selectively loading only the components you need.

## Problem
Claude Code loads all MCP servers and configurations by default, consuming 22%+ tokens before you even start. This tool allows you to:
- Start with minimal configurations (<5% tokens)
- Load components on-demand during your session
- Manage reusable agents, commands, and output styles
- Sync configurations across machines via GitHub

## Quick Start

```bash
# Install globally
cd ~/code/claude-setup
uv tool install .

# Use anywhere
cd ~/code/my-project
claude-manager
```

## Features

- **Token Optimization**: Start with <5% token usage instead of 22%+
- **TUI Interface**: Space-bar selection with real-time token calculation
- **Project Detection**: Smart handling of new vs existing projects
- **GitHub Sync**: Upload/download configurations
- **Component Library**: Reusable agents, commands, and output styles

## Structure

```
claude-setup/
├── agents/           # Reusable agent definitions (.md)
├── commands/         # Command templates (.md)
├── output-styles/    # Response style configurations (.md)
├── mcp-servers/      # MCP server configurations
├── documentation/    # Usage guides and templates
└── claude-manager.py # Main TUI application
```

## Installation

1. Clone to `~/code/claude-setup`
2. Run `uv tool install .`
3. Use `claude-manager` from any project directory