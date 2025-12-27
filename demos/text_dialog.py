#!/usr/bin/env python3
"""Demo: Text Dialog (Text Viewer/Editor)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, TextOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()

    sample_text = """Python Zenity Wrapper - Text Dialog Demo

This is a text dialog that can display large amounts of text.

Features:
- Display formatted text
- Scrollable content
- Optional editing mode
- Can load from files

This demo shows the text in editable mode.
Feel free to modify this text and click OK to see your changes!

Tips:
1. Use Ctrl+A to select all
2. Use Ctrl+C to copy
3. Use Ctrl+V to paste
4. Edit the text and click OK to submit

The text dialog is perfect for:
• Displaying license agreements
• Showing logs or reports
• Editing configuration files
• Viewing README files
"""

    edited_text = zenity.text(
        sample_text,
        TextOptions(
            title="Text Editor Demo",
            editable=True,
            width=600,
            height=500
        )
    )

    if edited_text:
        if edited_text != sample_text:
            print("✓ Text was modified!")
            print(f"\nNew text ({len(edited_text)} characters):")
            print("-" * 60)
            print(edited_text[:200] + "..." if len(edited_text) > 200 else edited_text)
            print("-" * 60)
            sys.exit(0)
        else:
            print("✓ Text was not modified")
            sys.exit(0)
    else:
        print("✗ Dialog was cancelled")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
