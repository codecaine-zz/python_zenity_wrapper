#!/usr/bin/env python3
"""Demo: Database Connection Form"""

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
        FormField(
            type='combo',
            label='Database Type',
            values=['PostgreSQL', 'MySQL', 'SQLite', 'MongoDB', 'Redis', 'SQL Server']
        ),
        FormField(type='entry', label='Host'),
        FormField(type='entry', label='Port'),
        FormField(type='entry', label='Database Name'),
        FormField(type='entry', label='Username'),
        FormField(type='password', label='Password'),
        FormField(
            type='combo',
            label='SSL Mode',
            values=['disable', 'require', 'verify-ca', 'verify-full']
        ),
        FormField(type='entry', label='Connection Timeout (seconds)')
    ],
    FormsOptions(
        title="Database Connection",
        text="Configure database connection settings:",
        separator="|",
        width=550,
        height=600
    )
)

    if result.button == 'ok' and result.values:
        db_type, host, port, db_name, username, password, ssl_mode, timeout = result.values
        
        # Validation
        if not host or not db_name or not username:
            print("✗ Error: Host, database name, and username are required", file=sys.stderr)
            sys.exit(1)
        
        if port and not port.isdigit():
            print("✗ Error: Port must be a number", file=sys.stderr)
            sys.exit(1)
        
        if timeout and not timeout.isdigit():
            print("✗ Error: Timeout must be a number", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*60)
        print("✓ DATABASE CONNECTION CONFIGURATION")
        print("="*60)
        print(f"Database Type: {db_type}")
        print(f"Host: {host}")
        print(f"Port: {port}")
        print(f"Database: {db_name}")
        print(f"Username: {username}")
        print(f"Password: {'*' * len(password)}")
        print(f"SSL Mode: {ssl_mode}")
        print(f"Timeout: {timeout} seconds")
        print("="*60)
        
        # Generate connection string (example)
        if db_type == 'PostgreSQL':
            conn_str = f"postgresql://{username}:****@{host}:{port}/{db_name}?sslmode={ssl_mode}"
            print(f"\nConnection String:\n{conn_str}")
        elif db_type == 'MySQL':
            conn_str = f"mysql://{username}:****@{host}:{port}/{db_name}"
            print(f"\nConnection String:\n{conn_str}")
        
        print("\n✓ Configuration saved successfully!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Database configuration cancelled")
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
