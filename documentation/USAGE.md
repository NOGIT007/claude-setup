# Usage Guide

## Basic Workflow

### Starting Claude Manager
```bash
# From any project directory
cd ~/code/my-project
claude-manager

# Or specify a project path
claude-manager --project ~/code/my-project
```

### TUI Navigation

#### Keyboard Controls
- **Space**: Toggle component selection (✓/✗)
- **↑↓**: Navigate between components
- **Enter**: Same as 'g' - Generate configuration
- **g**: Generate CLAUDE.md file
- **s**: Sync with GitHub (planned)
- **u**: Upload to GitHub (planned)
- **d**: Download from GitHub (planned)
- **q**: Quit application

#### Visual Interface
```
┌─────────────────────────────────────────────────┐
│          Claude Setup Manager v1.0              │
├─────────────────────────────────────────────────┤
│ Project: my-project (New)                      │
│ Token Usage: 3,500 (~1.8%)                     │
├─────────────────────────────────────────────────┤
│ AGENTS:                                         │
│ [✓] test-runner                                │
│ [ ] code-reviewer                              │
│ [ ] deployment-helper                          │
│                                                 │
│ MCP SERVERS:                                    │
│ [ ] github (13.5k tokens)                     │
│ [✓] playwright (12.8k tokens)                 │
└─────────────────────────────────────────────────┘
```

## Component Types

### 1. Agents
Specialized assistants for specific tasks:
- **code-reviewer**: Reviews code quality and security
- **test-runner**: Runs tests and analyzes results
- **deployment-helper**: Assists with Cloud Run deployments
- **security-scanner**: Defensive security analysis

### 2. Commands
Pre-configured command sets:
- **git-workflow**: Git commands and best practices
- **testing**: Testing commands for various frameworks
- **deployment**: Cloud Run deployment procedures
- **database**: Database management commands

### 3. Output Styles
Response formatting preferences:
- **minimal**: Ultra-concise responses (<4 lines)
- **concise**: Balanced brief responses
- **verbose**: Detailed explanations with context
- **debug**: Technical responses with debugging info

### 4. MCP Servers
Optional tool servers (load on-demand):
- **github**: Repository operations (13.5k tokens)
- **playwright**: Browser automation (12.8k tokens)
- **neo4j-aura**: Graph database queries (1.4k tokens)
- **context7**: Library documentation (1.3k tokens)
- **sequential-thinking**: Advanced reasoning (1.3k tokens)

## Token Optimization Strategy

### Default Approach: Minimal Loading
- Start with 0 MCP servers loaded
- Select only essential components
- Keep initial usage under 5% (10k tokens)

### On-Demand Loading
Instead of loading all MCPs at startup, use trigger phrases:
- "load github mcp" → Loads GitHub tools when ready to commit
- "load playwright" → Loads browser automation for testing
- "need documentation" → Loads Context7 for library docs

### Example Configurations

#### Minimal Setup (New Project)
```
Selected: minimal output style
Token Usage: ~100 tokens (0.05%)
```

#### Web Development
```
Selected: test-runner, playwright MCP, concise style
Token Usage: ~13k tokens (6.5%)
```

#### Full Development Suite
```
Selected: all agents, github + playwright MCPs
Token Usage: ~27k tokens (13.5%)
```

## Project Scenarios

### New Project
1. Run `claude-manager` in project directory
2. Select minimal components for your workflow
3. Generate CLAUDE.md
4. Load additional MCPs during session as needed

### Existing Project
1. Tool detects existing `.claude/CLAUDE.md`
2. Shows current configuration
3. Options to:
   - **Merge**: Add new components to existing
   - **Replace**: Start fresh configuration
   - **Backup**: Save current before replacing

### Updating Configuration
1. Run `claude-manager` again anytime
2. Modify component selections
3. Regenerate CLAUDE.md
4. Previous version backed up automatically

## Generated CLAUDE.md Example

```markdown
# Project Configuration
## Token Optimization
Estimated usage: 3,500 tokens (~1.8%)

## MCP Servers
Load only when needed:
- playwright: Browser automation and testing
  Load when: test ui, browser, screenshot

## Active Components
### Agents
- test-runner

### Output Style
- minimal

## Instructions
This configuration keeps initial token usage minimal.
Load MCP servers on-demand during your session by saying:
- 'load playwright' for testing
- 'load github mcp' when ready to commit
```

## Best Practices

### Token Management
1. **Start minimal**: Begin with no MCP servers
2. **Add incrementally**: Load tools only when needed
3. **Monitor usage**: Watch the token display
4. **Review regularly**: Update configuration as project evolves

### Component Selection
1. **Agents**: Choose based on current task phase
2. **Commands**: Include relevant tech stack commands
3. **Output Style**: Match your preference and urgency
4. **MCP Servers**: Load sparingly, use trigger phrases

### Workflow Integration
1. **Project Start**: Use minimal configuration
2. **Development**: Add test-runner, relevant commands
3. **Testing Phase**: Load playwright if needed
4. **Deployment**: Add deployment-helper, github MCP
5. **Maintenance**: Adjust based on current needs