#!/usr/bin/env python3
"""Demo: Entry Dialog (Text Input)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, EntryOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    name = zenity.entry(
        "Please enter your full name:",
        EntryOptions(
            title="Text Input",
            entry_text="John Doe"
        )
    )
    
    if name:
        print(f"✓ User entered: {name}")
        sys.exit(0)
    else:
        print("✗ User cancelled the dialog")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
