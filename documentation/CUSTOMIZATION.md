# Customization Guide

## Adding New Components

### Creating Custom Agents

1. **Create agent file**
   ```bash
   cd ~/code/claude-setup/agents
   touch my-custom-agent.md
   ```

2. **Agent template**
   ```markdown
   # My Custom Agent

   ## Description
   Brief description of what this agent does.

   ## Configuration
   When to use this agent.

   ## Instructions
   When activated, this agent will:
   1. First task
   2. Second task
   3. Third task

   ## Token Usage
   Estimated: ~0.3k tokens

   ## Usage
   Add this line to your CLAUDE.md:
   ```
   ## Active Agents
   - my-custom-agent: Description of the agent
   ```
   ```

### Creating Custom Commands

1. **Create command file**
   ```bash
   cd ~/code/claude-setup/commands
   touch my-framework.md
   ```

2. **Command template**
   ```markdown
   # My Framework Commands

   ## Description
   Commands for working with MyFramework.

   ## Common Commands
   ```bash
   # Start development server
   my-framework serve

   # Run tests
   my-framework test

   # Build for production
   my-framework build
   ```

   ## Best Practices
   1. Use environment variables
   2. Follow framework conventions
   3. Test before deployment

   ## Token Usage
   Estimated: ~0.2k tokens
   ```

### Creating Custom Output Styles

1. **Create style file**
   ```bash
   cd ~/code/claude-setup/output-styles
   touch technical.md
   ```

2. **Style template**
   ```markdown
   # Technical Output Style

   ## Description
   Highly technical responses with code examples.

   ## Instructions
   When this style is active:
   1. Include code snippets
   2. Reference documentation
   3. Provide technical depth
   4. Use industry terminology

   ## Examples
   - Include file paths and line numbers
   - Show command outputs
   - Reference specific APIs

   ## Token Usage
   Estimated: ~0.2k tokens
   ```

## MCP Server Configuration

### Adding New MCP Server

1. **Create server directory**
   ```bash
   cd ~/code/claude-setup/mcp-servers
   mkdir my-mcp-server
   ```

2. **Create configuration**
   ```bash
   cd my-mcp-server
   cat > config.json << 'EOF'
   {
     "name": "my-mcp-server",
     "description": "Custom MCP server for specific tasks",
     "token_usage": 2000,
     "tools_count": 5,
     "category": "custom",
     "use_cases": [
       "Custom task 1",
       "Custom task 2"
     ],
     "when_to_load": [
       "custom trigger",
       "specific keyword"
     ],
     "estimated_tokens": "2.0k tokens"
   }
   EOF
   ```

### Token Usage Calculation

MCP server token usage includes:
- Tool definitions (~100-200 tokens per tool)
- Documentation strings
- Parameter descriptions
- Example usage

**Estimation formula:**
```
Total = (tools_count × 200) + overhead
```

## Configuration Files

### config.yaml Customization

```yaml
# Custom token limits
token_limits:
  warning_threshold: 8000   # Warn at 8k tokens
  error_threshold: 15000    # Error at 15k tokens

# Custom component estimates
component_estimates:
  agents: 300               # Higher estimate for custom agents
  commands: 200
  output_styles: 150

# Custom MCP triggers
mcp_triggers:
  my-mcp-server:
    - "my custom trigger"
    - "specific task"
```

### Project-Specific Overrides

Create `.claude-setup.yaml` in your project:
```yaml
# Project-specific configuration
preferred_agents:
  - test-runner
  - my-custom-agent

preferred_mcp_servers:
  - github
  - my-mcp-server

default_output_style: technical

# Override token estimates
token_overrides:
  github: 10000  # Lower estimate for this project
```

## Advanced Customization

### Custom Component Categories

1. **Add new category directory**
   ```bash
   mkdir ~/code/claude-setup/workflows
   ```

2. **Update claude_manager.py**
   ```python
   # In load_components method
   components = {
       "agents": [],
       "commands": [],
       "output-styles": [],
       "workflows": []  # Add new category
   }
   ```

### Template Management

Create project templates in `documentation/templates/`:

**FastAPI Template**
```bash
mkdir -p documentation/templates/fastapi
cat > documentation/templates/fastapi/CLAUDE.md << 'EOF'
# FastAPI Project Configuration

## Recommended Components
- test-runner (for pytest)
- deployment-helper (for Cloud Run)
- github (for CI/CD)

## FastAPI Specific
- Use pytest for testing
- Follow FastAPI best practices
- Deploy to Cloud Run with proper health checks
EOF
```

### GitHub Sync Customization

When GitHub sync is implemented, customize:

```yaml
# config.yaml
github:
  sync_components:
    - agents
    - commands
    - output-styles
  exclude_personal:
    - my-secret-agent.md
  auto_sync: false
```

## Distribution

### Sharing Custom Components

1. **Fork the repository**
   ```bash
   git clone https://github.com/NOGIT007/claude-setup.git
   cd claude-setup
   git remote add upstream https://github.com/NOGIT007/claude-setup.git
   ```

2. **Add your components**
   ```bash
   # Add custom agents, commands, etc.
   git add agents/my-agent.md
   git commit -m "Add custom agent for my-framework"
   ```

3. **Create pull request**
   ```bash
   git push origin main
   # Create PR on GitHub
   ```

### Private Component Repository

Create your own component repository:
```bash
git clone https://github.com/NOGIT007/claude-setup.git my-claude-setup
cd my-claude-setup
git remote set-url origin https://github.com/yourusername/my-claude-setup.git

# Add private components
# Push to your private repo
```

## Integration Examples

### VS Code Integration

Create VS Code task in `.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Claude Setup",
      "type": "shell",
      "command": "claude-manager",
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

### Shell Alias

Add to your `.zshrc` or `.bashrc`:
```bash
alias cs='claude-manager'
alias csd='claude-manager --project .'
```