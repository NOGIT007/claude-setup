#!/bin/bash
# Simple wrapper to run claude-manager with correct PATH

export PATH="$HOME/.local/bin:$PATH"
claude-manager "$@"