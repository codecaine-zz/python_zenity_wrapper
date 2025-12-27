#!/usr/bin/env python3
"""Demo: Question Dialog"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, QuestionOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    answer = zenity.question(
        "Do you want to proceed with this operation?",
        QuestionOptions(
            title="Confirmation",
            ok_label="Yes, Proceed",
            cancel_label="No, Cancel"
        )
    )
    
    if answer:
        print("✓ User clicked: Yes, Proceed")
        sys.exit(0)
    else:
        print("✗ User clicked: No, Cancel")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
