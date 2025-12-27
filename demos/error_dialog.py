#!/usr/bin/env python3
"""Demo: Error Dialog"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, InfoOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    zenity.error(
        "This is an error message.\n\nError dialogs are used to notify users about errors or failures.",
        InfoOptions(
            title="Error",
            width=400
        )
    )
    
    print("✓ Error dialog displayed successfully!")
    sys.exit(0)
    
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
