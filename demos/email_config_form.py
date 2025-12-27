#!/usr/bin/env python3
"""Demo: Email Configuration Form"""

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
        FormField(type='entry', label='Your Name'),
        FormField(type='entry', label='Email Address'),
        FormField(
            type='combo',
            label='Email Provider',
            values=['Gmail', 'Outlook', 'Yahoo', 'iCloud', 'Custom SMTP']
        ),
        FormField(type='entry', label='SMTP Server'),
        FormField(type='entry', label='SMTP Port'),
        FormField(type='entry', label='Username'),
        FormField(type='password', label='Password/App Password'),
        FormField(
            type='combo',
            label='Encryption',
            values=['SSL/TLS', 'STARTTLS', 'None']
        ),
        FormField(type='entry', label='Reply-To Email (optional)')
    ],
    FormsOptions(
        title="Email Configuration",
        text="Configure your email account:",
        separator="|",
        width=550,
        height=650
    )
)

    if result.button == 'ok' and result.values:
        name, email, provider, smtp_server, smtp_port, username, password, encryption, reply_to = result.values
        
        # Validation
        if not email or '@' not in email:
            print("✗ Error: Valid email address is required", file=sys.stderr)
            sys.exit(1)
        
        if not smtp_server or not smtp_port:
            print("✗ Error: SMTP server and port are required", file=sys.stderr)
            sys.exit(1)
        
        if not smtp_port.isdigit():
            print("✗ Error: SMTP port must be a number", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*60)
        print("✓ EMAIL CONFIGURATION")
        print("="*60)
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Provider: {provider}")
        print(f"\nSMTP Settings:")
        print(f"  Server: {smtp_server}")
        print(f"  Port: {smtp_port}")
        print(f"  Username: {username}")
        print(f"  Password: {'*' * len(password)}")
        print(f"  Encryption: {encryption}")
        if reply_to:
            print(f"\nReply-To: {reply_to}")
        print("="*60)
        
        # Provide common SMTP suggestions
        if provider == 'Gmail':
            print("\n📧 Gmail Tips:")
            print("  • Use smtp.gmail.com:587 (STARTTLS) or smtp.gmail.com:465 (SSL)")
            print("  • Enable 'Less secure app access' or use App Password")
        elif provider == 'Outlook':
            print("\n📧 Outlook Tips:")
            print("  • Use smtp.office365.com:587 (STARTTLS)")
            print("  • Use your Microsoft account credentials")
        
        print("\n✓ Email configuration saved successfully!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Email configuration cancelled")
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
