# Git Workflow Commands

## Description
Standard git workflow commands and best practices for development.

## Common Commands

### Basic Workflow
```bash
# Check status
git status

# Add changes
git add .

# Commit with message
git commit -m "feat: add new feature"

# Push to remote
git push
```

### Branch Management
```bash
# Create new branch
git checkout -b feature/new-feature

# Switch branches
git checkout main

# Merge branch
git merge feature/new-feature

# Delete branch
git branch -d feature/new-feature
```

### Commit Message Conventions
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks
- `refactor:` - Code refactoring

### Token Usage
Estimated: ~0.1k tokens

## Usage
Add this line to your CLAUDE.md for git workflow support:
```
## Active Commands
- git-workflow: Standard git commands and best practices
```