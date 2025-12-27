#!/usr/bin/env python3
"""Demo: Network Settings Form"""

import sys
sys.path.insert(0, '..')
from zenity_wrapper import Zenity, FormField, FormsOptions

zenity = Zenity()

result = zenity.forms(
    [
        FormField(type='entry', label='Network Name'),
        FormField(
            type='combo',
            label='IP Configuration',
            values=['DHCP (Automatic)', 'Static IP']
        ),
        FormField(type='entry', label='IP Address'),
        FormField(type='entry', label='Subnet Mask'),
        FormField(type='entry', label='Default Gateway'),
        FormField(type='entry', label='Primary DNS'),
        FormField(type='entry', label='Secondary DNS'),
        FormField(
            type='combo',
            label='Connection Type',
            values=['Wired (Ethernet)', 'Wireless (WiFi)', 'VPN', 'PPPoE', 'Cellular']
        ),
        FormField(type='entry', label='MAC Address'),
        FormField(type='entry', label='MTU Size'),
        FormField(
            type='combo',
            label='Proxy',
            values=['No Proxy', 'HTTP Proxy', 'HTTPS Proxy', 'SOCKS4', 'SOCKS5', 'Auto-detect']
        ),
        FormField(type='entry', label='Proxy Server:Port')
    ],
    FormsOptions(
        title="Network Configuration",
        text="Configure network settings:",
        separator="|",
        show_header=True,
        width=600,
        height=750
    )
)

if result.button == 'ok' and result.values:
    name, ip_config, ip_addr, subnet, gateway, dns1, dns2, conn_type, mac, mtu, proxy, proxy_server = result.values
    
    print("\n" + "="*60)
    print("NETWORK CONFIGURATION")
    print("="*60)
    print(f"Network Name: {name}")
    print(f"Connection Type: {conn_type}")
    print(f"IP Configuration: {ip_config}")
    
    if ip_config == 'Static IP':
        print(f"\nIP Settings:")
        print(f"  IP Address: {ip_addr}")
        print(f"  Subnet Mask: {subnet}")
        print(f"  Gateway: {gateway}")
    
    print(f"\nDNS Servers:")
    print(f"  Primary: {dns1}")
    print(f"  Secondary: {dns2}")
    
    if mac:
        print(f"\nMAC Address: {mac}")
    
    if mtu:
        print(f"MTU Size: {mtu}")
    
    if proxy != 'No Proxy':
        print(f"\nProxy Configuration:")
        print(f"  Type: {proxy}")
        if proxy_server:
            print(f"  Server: {proxy_server}")
    
    print("\n" + "="*60)
    print("\n✓ Network settings saved!")
    print("  Changes will take effect after reconnecting.")
elif result.button == 'cancel':
    print("Network configuration cancelled")
