#!/usr/bin/env python3
"""Demo: Scale Dialog (Slider)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, ScaleOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    volume = zenity.scale(
        "Adjust the volume level:",
        ScaleOptions(
            title="Volume Control",
            value=50,
            min_value=0,
            max_value=100,
            step=5
        )
    )
    
    if volume is not None:
        print(f"✓ Volume set to: {volume}%")
        # Visual representation
        bars = '█' * (volume // 5)
        print(f"Volume: [{bars:<20}] {volume}%")
        sys.exit(0)
    else:
        print("✗ User cancelled")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
