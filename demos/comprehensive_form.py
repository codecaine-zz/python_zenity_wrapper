#!/usr/bin/env python3
"""Demo: Comprehensive Form (All Field Types)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, FormField, FormsOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    print("This demo showcases ALL 6 form field types in one form.")
    print("Fill out the registration form...\n")

    result = zenity.forms(
    [
        FormField(type='entry', label='Full Name'),
        FormField(type='password', label='Password'),
        FormField(type='multiline', label='Bio'),
        FormField(type='calendar', label='Birth Date'),
        FormField(
            type='combo',
            label='Gender',
            values=['Male', 'Female', 'Non-binary', 'Prefer not to say']
        ),
        FormField(
            type='combo',
            label='Country',
            values=['USA', 'Canada', 'UK', 'Australia', 'Germany', 'France', 'Japan', 'Brazil', 'India', 'China']
        )
    ],
    FormsOptions(
        title="Complete Registration",
        text="All field types demonstrated:",
        separator="||",
        forms_date_format="%Y-%m-%d",
        show_header=True,
        width=600,
        height=650
    )
    )

    if result.button == 'ok' and result.values:
        name, password, bio, birth_date, gender, country = result.values
        
        # Validation
        if not name or not password:
            print("✗ Error: Name and password are required", file=sys.stderr)
            sys.exit(1)
        
        if len(password) < 8:
            print("✗ Warning: Password should be at least 8 characters", file=sys.stderr)
        
        print("\n" + "="*60)
        print("✓ REGISTRATION COMPLETE - ALL FIELD TYPES")
        print("="*60)
        print(f"\n✓ Entry Field - Name: {name}")
        print(f"✓ Password Field - Password: {'*' * len(password)} ({len(password)} chars)")
        print(f"✓ Multiline Field - Bio: {bio[:50]}{'...' if len(bio) > 50 else ''}")
        print(f"✓ Calendar Field - Birth Date: {birth_date}")
        print(f"✓ Combo Field - Gender: {gender}")
        print(f"✓ List Field - Country: {country}")
        print("\n" + "="*60)
        print("\nAll 6 form field types successfully captured!")
        sys.exit(0)
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
