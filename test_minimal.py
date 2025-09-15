#!/usr/bin/env python3
"""Minimal test to debug the widget ID issue"""

import sys
from pathlib import Path
import os

# Change to project directory first
os.chdir(Path.home() / "code" / "test-project")

# Add the current directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

# Import and test
try:
    from claude_manager import ComponentSelector, Component

    # Test component creation
    components = [
        Component(
            name="debug",
            category="output-styles",
            description="Test component",
            token_usage=200,
            file_path=Path("/fake/path")
        )
    ]

    # Test widget creation
    selector = ComponentSelector("Output Styles", components, set())

    print("✅ ComponentSelector created successfully")
    print(f"Title: '{selector.title}'")
    print(f"Components: {[c.name for c in selector.components]}")

    # Test ID generation manually
    title_clean = selector.title.lower().replace(' ', '_').replace('-', '_')
    name_clean = components[0].name.replace('-', '_').replace(' ', '_')
    expected_id = f"{title_clean}_{name_clean}"
    print(f"Expected ID: '{expected_id}'")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()