# Installation Guide

## Prerequisites

- Python 3.8 or higher
- `uv` package manager
- Git

## Quick Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NOGIT007/claude-setup.git ~/code/claude-setup
   cd ~/code/claude-setup
   ```

2. **Install globally using uv**
   ```bash
   uv tool install .
   ```

3. **Update your PATH** (if needed)
   ```bash
   export PATH="/Users/$USER/.local/bin:$PATH"
   # Add to your shell profile (.bashrc, .zshrc, etc.)
   echo 'export PATH="/Users/$USER/.local/bin:$PATH"' >> ~/.zshrc
   ```

4. **Verify installation**
   ```bash
   claude-manager --help
   ```

## Alternative Installation Methods

### Manual Installation
```bash
cd ~/code/claude-setup
python -m pip install .
```

### Development Installation
```bash
cd ~/code/claude-setup
uv tool install --editable .
```

## First Time Setup

1. **Navigate to any project**
   ```bash
   cd ~/code/my-project
   ```

2. **Run claude-manager**
   ```bash
   claude-manager
   ```

3. **Select components** using:
   - **Space**: Toggle selection
   - **↑↓**: Navigate
   - **g**: Generate CLAUDE.md
   - **q**: Quit

## New Machine Setup

On a new Mac, follow these steps:

1. **Install Python and uv**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and install claude-setup**
   ```bash
   git clone https://github.com/NOGIT007/claude-setup.git ~/code/claude-setup
   cd ~/code/claude-setup
   uv tool install .
   ```

3. **Update shell PATH**
   ```bash
   uv tool update-shell
   ```

4. **Ready to use**
   ```bash
   claude-manager
   ```

## Troubleshooting

### Command not found
- Ensure `~/.local/bin` is in your PATH
- Run `uv tool update-shell`

### Permission errors
- Make sure you have write access to `~/.local/`
- Try `chmod +x ~/.local/bin/claude-manager`

### Missing dependencies
- Run `uv tool uninstall claude-manager`
- Then `uv tool install .` again

### Python version issues
- Ensure Python 3.8+ is installed
- Check with `python --version`