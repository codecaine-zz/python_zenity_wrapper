#!/usr/bin/env python3
"""Demo: List Dialog (Simple Selection)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, ListOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    fruit = zenity.list(
        "Choose your favorite fruit:",
        ["Fruit", "Color", "Calories"],
        [
            ["Apple", "Red", "95"],
            ["Banana", "Yellow", "105"],
            ["Orange", "Orange", "62"],
            ["Grape", "Purple", "62"],
            ["Strawberry", "Red", "49"]
        ],
        ListOptions(
            title="Fruit Selection",
            width=500,
            height=300
        )
    )
    
    if fruit:
        print(f"✓ You selected: {fruit}")
        sys.exit(0)
    else:
        print("✗ No selection made")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
