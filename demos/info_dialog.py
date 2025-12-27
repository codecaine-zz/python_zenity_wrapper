#!/usr/bin/env python3
"""Demo: Info Dialog"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, InfoOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    zenity.info(
        "This is an information message.\n\nInfo dialogs are used to display general information to the user.",
        InfoOptions(
            title="Information",
            width=400
        )
    )
    
    print("✓ Info dialog displayed successfully!")
    sys.exit(0)
    
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
