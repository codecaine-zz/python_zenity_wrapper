#!/usr/bin/env python3
"""Demo: Radio List Dialog (Single Selection)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, ListOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()

    size = zenity.list(
    "Select your T-shirt size:",
    ["Select", "Size", "Chest (inches)", "Length (inches)"],
    [
        [False, "Small", "34-36", "27"],
        [True, "Medium", "38-40", "28"],
        [False, "Large", "42-44", "29"],
        [False, "X-Large", "46-48", "30"],
        [False, "XX-Large", "50-52", "31"],
    ],
    ListOptions(
        title="Size Selection",
        radiolist=True,
        width=500,
        height=350
    )
)

    if size:
        print(f"✓ Selected size: {size}")
        sys.exit(0)
    else:
        print("✗ No size selected")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
