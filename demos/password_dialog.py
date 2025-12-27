#!/usr/bin/env python3
"""Demo: Password Dialog"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, PasswordOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    # Simple password
    print("Demo 1: Simple password entry")
    password = zenity.password(
        PasswordOptions(title="Enter Password")
    )
    
    if password:
        print(f"✓ Password entered (length: {len(password)} characters)")
    else:
        print("✗ User cancelled")
        sys.exit(1)
    
    print("\nDemo 2: Username + Password entry")
    credentials = zenity.password(
        PasswordOptions(
            username=True,
            title="Login Credentials"
        )
    )
    
    if credentials:
        if '|' in credentials:
            username, pwd = credentials.split('|', 1)
            print(f"✓ Username: {username}")
            print(f"✓ Password: (length: {len(pwd)} characters)")
            sys.exit(0)
        else:
            print(f"✓ Credentials entered: {credentials}")
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
