# Quick Start Guide

## ✅ Issues Fixed
- MCP server configuration errors resolved
- Widget ID naming issues fixed
- PATH setup improved

## 🚀 How to Use claude-manager

### Option 1: Add PATH to your shell (Recommended)
```bash
# Add to your ~/.zshrc (already done for you)
export PATH="$HOME/.local/bin:$PATH"

# Reload your shell
source ~/.zshrc

# Now you can use it anywhere
cd ~/code/any-project
claude-manager
```

### Option 2: Use full path
```bash
# Direct path to the tool
~/.local/bin/claude-manager
```

### Option 3: Use the wrapper script
```bash
# From the claude-setup directory
cd ~/code/claude-setup
./run.sh
```

## 🎯 Testing the Tool

1. **Start a new terminal session** (to pick up the PATH changes)

2. **Navigate to any project**:
   ```bash
   cd ~/code/any-project
   claude-manager
   ```

3. **You should see the TUI interface**:
   ```
   ┌─────────────────────────────────────────────────┐
   │          Claude Setup Manager v1.0              │
   ├─────────────────────────────────────────────────┤
   │ Project: your-project (New)                    │
   │ Token Usage: 0 (~0.0%)                         │
   ├─────────────────────────────────────────────────┤
   │ AGENTS:                                         │
   │ [ ] code-reviewer                              │
   │ [ ] test-runner                                │
   │ [ ] deployment-helper                          │
   │ [ ] security-scanner                           │
   │                                                 │
   │ COMMANDS:                                       │
   │ [ ] git-workflow                               │
   │ [ ] testing                                    │
   │ [ ] deployment                                 │
   │ [ ] database                                   │
   │                                                 │
   │ OUTPUT STYLES:                                  │
   │ [ ] minimal                                    │
   │ [ ] concise                                    │
   │ [ ] verbose                                    │
   │ [ ] debug                                      │
   │                                                 │
   │ MCP SERVERS:                                    │
   │ [ ] github (13.5k tokens)                     │
   │ [ ] playwright (12.8k tokens)                 │
   │ [ ] neo4j-aura (1.4k tokens)                  │
   │ [ ] context7 (1.3k tokens)                    │
   │ [ ] sequential-thinking (1.3k tokens)         │
   └─────────────────────────────────────────────────┘
   ```

## 🔧 Controls

- **Space**: Toggle selection (✓/✗)
- **↑↓**: Navigate between items
- **g** or **Enter**: Generate CLAUDE.md
- **q**: Quit

## 💡 Example Workflow

1. **Select minimal components**:
   - ✓ minimal (output style)
   - ✓ git-workflow (commands)
   - Leave MCP servers unselected for 0 tokens

2. **Press 'g'** to generate CLAUDE.md

3. **Result**: Your project now has optimized configuration!

## 🎯 Expected Results

- **Before**: Claude Code starts with 27% token usage (54k tokens)
- **After**: Claude Code starts with <1% token usage (<2k tokens)
- **Savings**: 95%+ token reduction!

## 🚨 Troubleshooting

### "command not found: claude-manager"
```bash
# Check PATH
echo $PATH | grep ".local/bin"

# If not found, add manually:
export PATH="$HOME/.local/bin:$PATH"

# Or use the wrapper:
cd ~/code/claude-setup && ./run.sh
```

### TUI doesn't start
```bash
# Check if installed correctly
ls -la ~/.local/bin/claude-manager

# Reinstall if needed
cd ~/code/claude-setup
uv tool uninstall claude-manager
uv tool install .
```

## ✅ Success!

Once working, you'll have:
- Minimal token usage on Claude Code startup
- Flexible component selection
- Automatic backup of configurations
- On-demand MCP server loading

Your Claude Code experience is now optimized! 🎉