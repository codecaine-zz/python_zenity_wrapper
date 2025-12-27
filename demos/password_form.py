#!/usr/bin/env python3
"""Demo: Password Form (Login Form)"""

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
        FormField(type='entry', label='Username'),
        FormField(type='password', label='Password'),
        FormField(type='password', label='Confirm Password')
    ],
    FormsOptions(
        title="User Registration",
        text="Create your account:",
        separator="|",
        width=450
    )
)

    if result.button == 'ok' and result.values:
        username, password, confirm = result.values
        
        # Validation
        if not username or not password or not confirm:
            print("✗ Error: All fields are required", file=sys.stderr)
            sys.exit(1)
        
        if len(password) < 8:
            print("✗ Error: Password must be at least 8 characters", file=sys.stderr)
            sys.exit(1)
        
        print("\n✓ Registration Form Submitted")
        print(f"Username: {username}")
        print(f"Password: {'*' * len(password)} ({len(password)} characters)")
        print(f"Confirm: {'*' * len(confirm)} ({len(confirm)} characters)")
        
        if password == confirm:
            print("\n✓ Passwords match!")
            sys.exit(0)
        else:
            print("\n✗ Passwords do not match!", file=sys.stderr)
            sys.exit(1)
    elif result.button == 'cancel':
        print("✗ Registration cancelled")
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
