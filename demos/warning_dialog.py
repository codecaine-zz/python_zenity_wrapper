#!/usr/bin/env python3
"""Demo: Warning Dialog"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, InfoOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    zenity.warning(
        "This is a warning message.\n\nWarning dialogs are used to alert users about potential issues.",
        InfoOptions(
            title="Warning",
            width=400
        )
    )
    
    print("✓ Warning dialog displayed successfully!")
    sys.exit(0)
    
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
