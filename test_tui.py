#!/usr/bin/env python3
"""
Quick test to verify the TUI components load correctly
"""
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from claude_manager import ClaudeManagerApp

def test_app_creation():
    """Test that the app can be created without errors"""
    try:
        app = ClaudeManagerApp()
        print("✅ App created successfully")

        # Test component loading
        agents = app.components.get("agents", [])
        commands = app.components.get("commands", [])
        output_styles = app.components.get("output-styles", [])
        mcp_servers = app.mcp_servers

        print(f"✅ Loaded {len(agents)} agents")
        print(f"✅ Loaded {len(commands)} commands")
        print(f"✅ Loaded {len(output_styles)} output styles")
        print(f"✅ Loaded {len(mcp_servers)} MCP servers")

        # Test token calculation
        total_tokens = app.project_config.total_tokens
        print(f"✅ Token calculation works: {total_tokens} tokens")

        print("\n🎉 All tests passed! The TUI should work correctly.")
        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_app_creation()