#!/usr/bin/env python3
"""Demo: API Configuration Form"""

import sys
sys.path.insert(0, '..')
from zenity_wrapper import Zenity, FormField, FormsOptions

zenity = Zenity()

result = zenity.forms(
    [
        FormField(type='entry', label='API Name'),
        FormField(type='entry', label='Base URL'),
        FormField(type='entry', label='API Key'),
        FormField(type='password', label='API Secret'),
        FormField(
            type='combo',
            label='Authentication Type',
            values=['API Key', 'Bearer Token', 'Basic Auth', 'OAuth 2.0', 'Custom Header']
        ),
        FormField(
            type='combo',
            label='API Version',
            values=['v1', 'v2', 'v3', 'latest', 'beta']
        ),
        FormField(type='entry', label='Rate Limit (requests/minute)'),
        FormField(type='entry', label='Timeout (seconds)'),
        FormField(type='entry', label='Retry Attempts'),
        FormField(
            type='combo',
            label='Response Format',
            values=['JSON', 'XML', 'YAML', 'CSV', 'Protocol Buffers']
        ),
        FormField(type='multiline', label='Custom Headers (JSON)')
    ],
    FormsOptions(
        title="API Configuration",
        text="Configure API connection settings:",
        separator="|",
        show_header=True,
        width=600,
        height=700
    )
)

if result.button == 'ok' and result.values:
    api_name, base_url, api_key, api_secret, auth_type, version, rate_limit, timeout, retries, format_type, headers = result.values
    
    print("\n" + "="*60)
    print("API CONFIGURATION")
    print("="*60)
    print(f"API Name: {api_name}")
    print(f"Base URL: {base_url}")
    print(f"Version: {version}")
    
    print(f"\n🔐 Authentication:")
    print(f"  Type: {auth_type}")
    print(f"  API Key: {api_key[:10]}...{api_key[-4:] if len(api_key) > 14 else ''}")
    print(f"  API Secret: {'*' * len(api_secret)}")
    
    print(f"\n⚙️ Settings:")
    print(f"  Rate Limit: {rate_limit} requests/minute")
    print(f"  Timeout: {timeout} seconds")
    print(f"  Retry Attempts: {retries}")
    print(f"  Response Format: {format_type}")
    
    if headers:
        print(f"\n📋 Custom Headers:")
        print(f"  {headers[:80]}{'...' if len(headers) > 80 else ''}")
    
    print("\n" + "="*60)
    
    # Generate example request
    print(f"\nExample Request:")
    print(f"  curl -X GET '{base_url}/{version}/endpoint' \\")
    print(f"       -H 'Authorization: {auth_type} {api_key}' \\")
    print(f"       -H 'Content-Type: application/json'")
    
    print("\n✓ API configuration saved successfully!")
elif result.button == 'cancel':
    print("API configuration cancelled")
