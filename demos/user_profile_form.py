#!/usr/bin/env python3
"""Demo: User Profile Editor Form"""

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
        FormField(type='entry', label='Username'),
        FormField(type='entry', label='Email'),
        FormField(type='entry', label='Phone'),
        FormField(type='calendar', label='Date of Birth'),
        FormField(
            type='combo',
            label='Gender',
            values=['Male', 'Female', 'Non-binary', 'Prefer not to say']
        ),
        FormField(
            type='combo',
            label='Country',
            values=['United States', 'Canada', 'United Kingdom', 'Australia', 'Germany', 
                   'France', 'Japan', 'Brazil', 'India', 'China', 'Mexico', 'Spain', 'Italy']
        ),
        FormField(type='entry', label='City'),
        FormField(type='entry', label='Occupation'),
        FormField(type='multiline', label='Bio'),
        FormField(type='entry', label='Website/LinkedIn URL')
    ],
    FormsOptions(
        title="Edit User Profile",
        text="Update your profile information:",
        separator="|",
        forms_date_format="%Y-%m-%d",
        show_header=True,
        width=600,
        height=750
    )
    )
    
    if result.button == 'ok' and result.values:
        first, last, username, email, phone, dob, gender, country, city, occupation, bio, website = result.values
        
        # Validation
        if not first or not last or not username:
            print("✗ Error: First name, last name, and username are required", file=sys.stderr)
            sys.exit(1)
        
        if email and '@' not in email:
            print("✗ Warning: Email appears to be invalid", file=sys.stderr)
        
        print("\n" + "="*60)
        print("✓ USER PROFILE UPDATED")
        print("="*60)
        print(f"\n{first} {last} (@{username})")
        print(f"{occupation}")
        print(f"\n📧 {email}")
        print(f"📱 {phone}")
        print(f"🌍 {city}, {country}")
        print(f"🎂 Born: {dob}")
        print(f"⚧  Gender: {gender}")
        
        if website:
            print(f"🔗 {website}")
        
        if bio:
            print(f"\n📝 Bio:\n{bio}")
        
        print("\n" + "="*60)
        print("\n✓ Profile updated successfully!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Profile update cancelled")
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
