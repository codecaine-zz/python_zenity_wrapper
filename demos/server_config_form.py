#!/usr/bin/env python3
"""Demo: Server Configuration Form"""

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
        FormField(type='entry', label='Server Name'),
        FormField(type='entry', label='Hostname/IP'),
        FormField(type='entry', label='Port'),
        FormField(
            type='combo',
            label='Protocol',
            values=['HTTP', 'HTTPS', 'TCP', 'UDP', 'WebSocket', 'gRPC']
        ),
        FormField(
            type='combo',
            label='Environment',
            values=['Development', 'Staging', 'Production', 'Testing']
        ),
        FormField(type='entry', label='Max Connections'),
        FormField(type='entry', label='Timeout (seconds)'),
        FormField(
            type='combo',
            label='Log Level',
            values=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        ),
        FormField(type='entry', label='API Key (optional)'),
        FormField(type='multiline', label='Additional Config (JSON/YAML)')
    ],
    FormsOptions(
        title="Server Configuration",
        text="Configure server settings:",
        separator="|",
        show_header=True,
        width=600,
        height=700
    )
)

    if result.button == 'ok' and result.values:
        name, host, port, protocol, env, max_conn, timeout, log_level, api_key, config = result.values
        
        # Validation
        if not name or not host or not port:
            print("✗ Error: Server name, hostname, and port are required", file=sys.stderr)
            sys.exit(1)
        
        if not port.isdigit():
            print("✗ Error: Port must be a number", file=sys.stderr)
            sys.exit(1)
        
        if max_conn and not max_conn.isdigit():
            print("✗ Error: Max connections must be a number", file=sys.stderr)
            sys.exit(1)
        
        if timeout and not timeout.isdigit():
            print("✗ Error: Timeout must be a number", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*60)
        print("✓ SERVER CONFIGURATION")
        print("="*60)
        print(f"Server Name: {name}")
        print(f"Hostname/IP: {host}")
        print(f"Port: {port}")
        print(f"Protocol: {protocol}")
        print(f"Environment: {env}")
        print(f"\nPerformance Settings:")
        print(f"  Max Connections: {max_conn}")
        print(f"  Timeout: {timeout}s")
        print(f"  Log Level: {log_level}")
        
        if api_key:
            print(f"\nAPI Key: {api_key[:10]}...{api_key[-4:] if len(api_key) > 14 else ''}")
        
        if config:
            print(f"\nAdditional Configuration:")
            print(config[:100] + "..." if len(config) > 100 else config)
        
        print("\n" + "="*60)
        
        # Generate connection URL
        protocol_lower = protocol.lower()
        url = f"{protocol_lower}://{host}:{port}"
        print(f"\nConnection URL: {url}")
        print("\n✓ Server configuration saved successfully!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Server configuration cancelled")
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
