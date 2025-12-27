#!/usr/bin/env python3
"""Demo: Bug Report Form"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, FormField, FormsOptions
    from datetime import datetime
except ImportError as e:
    print(f"Error: Failed to import required modules: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()

    result = zenity.forms(
    [
        FormField(type='entry', label='Bug Title'),
        FormField(
            type='combo',
            label='Severity',
            values=['Critical', 'High', 'Medium', 'Low', 'Trivial']
        ),
        FormField(
            type='combo',
            label='Category',
            values=['UI/UX', 'Performance', 'Security', 'Data Loss', 'Crash', 'Feature', 'Other']
        ),
        FormField(type='multiline', label='Description'),
        FormField(type='multiline', label='Steps to Reproduce'),
        FormField(type='entry', label='Expected Behavior'),
        FormField(type='entry', label='Actual Behavior'),
        FormField(type='entry', label='Reporter Email')
    ],
    FormsOptions(
        title="Bug Report",
        text="Report a bug or issue:",
        separator="||",
        width=650,
        height=750
    )
)

    if result.button == 'ok' and result.values:
        title, severity, category, description, steps, expected, actual, email = result.values
        
        # Validation
        if not title or not description:
            print("✗ Error: Title and description are required", file=sys.stderr)
            sys.exit(1)
        
        if email and '@' not in email:
            print("✗ Warning: Email appears to be invalid", file=sys.stderr)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("\n" + "="*70)
        print("✓ BUG REPORT SUBMITTED")
        print("="*70)
        print(f"Report ID: BUG-{datetime.now().strftime('%Y%m%d%H%M%S')}")
        print(f"Timestamp: {timestamp}")
        print(f"\nTitle: {title}")
        print(f"Severity: {severity}")
        print(f"Category: {category}")
        print(f"\nDescription:\n{description}")
        print(f"\nSteps to Reproduce:\n{steps}")
        print(f"\nExpected Behavior: {expected}")
        print(f"Actual Behavior: {actual}")
        print(f"\nReporter: {email}")
        print("="*70)
        print("\n✓ Bug report submitted successfully!")
        print("  The development team will review this issue shortly.")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Bug report cancelled")
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
