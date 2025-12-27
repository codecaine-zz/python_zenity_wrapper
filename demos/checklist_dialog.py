#!/usr/bin/env python3
"""Demo: Checklist Dialog (Multiple Selection)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, ListOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:

    zenity = Zenity()
    
    toppings = zenity.list(
    "Select your pizza toppings:",
    ["Select", "Topping", "Price", "Calories"],
    [
        [False, "Cheese", "$1.00", "100"],
        [True, "Pepperoni", "$2.00", "150"],
        [False, "Mushrooms", "$1.50", "20"],
        [False, "Olives", "$1.50", "30"],
        [False, "Onions", "$1.00", "15"],
        [False, "Bell Peppers", "$1.25", "25"],
    ],
    ListOptions(
        title="Pizza Toppings",
        checklist=True,
        multiple=True,
        width=500,
        height=400
    )
)

    if toppings:
        print(f"✓ Selected toppings: {toppings}")
        if isinstance(toppings, list):
            print(f"Total selections: {len(toppings)}")
        else:
            print(f"Selected: {toppings}")
        sys.exit(0)
    else:
        print("✗ No toppings selected")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
