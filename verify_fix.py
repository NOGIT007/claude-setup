#!/usr/bin/env python3
"""
Test script to verify the widget ID fix is working
"""
import subprocess
import sys
import os
from pathlib import Path

def test_claude_manager():
    """Test that claude-manager starts without widget ID errors"""

    # Set up environment
    env = os.environ.copy()
    env['PATH'] = f"{Path.home()}/.local/bin:{env.get('PATH', '')}"

    # Change to test project
    test_project = Path.home() / "code" / "test-project"
    test_project.mkdir(parents=True, exist_ok=True)

    print("🧪 Testing claude-manager startup...")

    try:
        # Run claude-manager with a short timeout to test startup
        process = subprocess.Popen(
            ['claude-manager'],
            cwd=test_project,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Let it run for 2 seconds, then terminate
        try:
            stdout, stderr = process.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            process.terminate()
            stdout, stderr = process.communicate()

        # Check for widget ID errors
        if "BadIdentifier" in stderr:
            print("❌ Widget ID error still present:")
            print(stderr)
            return False
        elif "output styles-debug" in stderr:
            print("❌ Still generating invalid IDs")
            print(stderr)
            return False
        else:
            print("✅ No widget ID errors detected!")
            print("✅ TUI appears to start correctly")
            return True

    except FileNotFoundError:
        print("❌ claude-manager not found in PATH")
        print("Run: export PATH=\"$HOME/.local/bin:$PATH\"")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_claude_manager()
    sys.exit(0 if success else 1)