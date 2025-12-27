#!/usr/bin/env python3
"""Demo: Simple Form (Entry Fields)"""

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
        FormField(type='entry', label='First Name'),
        FormField(type='entry', label='Last Name'),
        FormField(type='entry', label='Email')
    ],
    FormsOptions(
        title="Contact Information",
        text="Please enter your contact details:",
        separator="|",
        width=500
    )
)

    if result.button == 'ok' and result.values:
        first_name, last_name, email = result.values
        
        # Basic validation
        if not first_name or not last_name:
            print("✗ Error: First name and last name are required", file=sys.stderr)
            sys.exit(1)
        
        if email and '@' not in email:
            print("✗ Warning: Email appears to be invalid", file=sys.stderr)
        
        print("\n✓ Form submitted successfully!")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Form cancelled by user")
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
