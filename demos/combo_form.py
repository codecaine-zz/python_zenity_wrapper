#!/usr/bin/env python3
"""Demo: Combo Form (Survey Form)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, FormField, FormsOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()

    result = zenity.forms(
    [
        FormField(type='entry', label='Full Name'),
        FormField(type='combo', label='Age Group', values=['18-25', '26-35', '36-45', '46-55', '56+']),
        FormField(type='combo', label='Education', values=['High School', 'Bachelor', 'Master', 'PhD', 'Other']),
        FormField(type='combo', label='Employment', values=['Employed', 'Self-Employed', 'Student', 'Retired', 'Unemployed'])
    ],
    FormsOptions(
        title="Survey Form",
        text="Please complete this quick survey:",
        separator="|",
        width=500,
        height=400
    )
)

    if result.button == 'ok' and result.values:
        name, age_group, education, employment = result.values
        
        # Validation
        if not name:
            print("✗ Error: Name is required", file=sys.stderr)
            sys.exit(1)
        
        print("\n✓ Survey Response:")
        print(f"Name: {name}")
        print(f"Age Group: {age_group}")
        print(f"Education: {education}")
        print(f"Employment Status: {employment}")
        print("\nThank you for completing the survey!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Survey cancelled")
        sys.exit(1)
    else:
        print("✗ No data received", file=sys.stderr)
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
