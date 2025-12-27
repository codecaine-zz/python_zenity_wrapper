#!/usr/bin/env python3
"""Demo: Backup Configuration Form"""

import sys
sys.path.insert(0, '..')
from zenity_wrapper import Zenity, FormField, FormsOptions

zenity = Zenity()

result = zenity.forms(
    [
        FormField(type='entry', label='Backup Name'),
        FormField(type='entry', label='Source Directory'),
        FormField(type='entry', label='Destination Directory'),
        FormField(
            type='combo',
            label='Backup Type',
            values=['Full', 'Incremental', 'Differential', 'Mirror']
        ),
        FormField(
            type='combo',
            label='Schedule',
            values=['Manual', 'Daily', 'Weekly', 'Monthly', 'On System Start', 'On Shutdown']
        ),
        FormField(
            type='combo',
            label='Compression',
            values=['None', 'ZIP', 'GZIP', 'BZIP2', 'XZ', '7Z']
        ),
        FormField(
            type='combo',
            label='Retention',
            values=['Keep All', 'Last 7 days', 'Last 30 days', 'Last 90 days', 'Last 365 days', 'Custom']
        ),
        FormField(type='entry', label='Max Backup Size (GB)'),
        FormField(type='entry', label='Exclude Patterns (comma-separated)'),
        FormField(type='entry', label='Email Notification (optional)')
    ],
    FormsOptions(
        title="Backup Configuration",
        text="Configure automatic backup settings:",
        separator="|",
        width=600,
        height=650
    )
)

if result.button == 'ok' and result.values:
    name, source, dest, backup_type, schedule, compression, retention, max_size, exclude, email = result.values
    
    print("\n" + "="*60)
    print("BACKUP CONFIGURATION")
    print("="*60)
    print(f"Backup Name: {name}")
    print(f"\nSource: {source}")
    print(f"Destination: {dest}")
    print(f"\nBackup Type: {backup_type}")
    print(f"Schedule: {schedule}")
    print(f"Compression: {compression}")
    print(f"Retention Policy: {retention}")
    print(f"Max Size: {max_size} GB")
    
    if exclude:
        print(f"\nExclude Patterns:")
        for pattern in exclude.split(','):
            print(f"  - {pattern.strip()}")
    
    if email:
        print(f"\nNotifications will be sent to: {email}")
    
    print("\n" + "="*60)
    print("\n✓ Backup configuration saved!")
    print(f"  Next backup: {schedule}")
elif result.button == 'cancel':
    print("Backup configuration cancelled")
