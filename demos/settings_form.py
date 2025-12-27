#!/usr/bin/env python3
"""Demo: Application Settings Form"""

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
        FormField(type='entry', label='App Name'),
        FormField(
            type='combo',
            label='Theme',
            values=['Light', 'Dark', 'Auto', 'High Contrast']
        ),
        FormField(
            type='combo',
            label='Language',
            values=['English', 'Spanish', 'French', 'German', 'Japanese', 'Chinese']
        ),
        FormField(
            type='combo',
            label='Font Size',
            values=['Small', 'Medium', 'Large', 'Extra Large']
        ),
        FormField(
            type='combo',
            label='Default Action',
            values=['Open Last File', 'Open New File', 'Show Welcome Screen', 'Restore Session']
        ),
        FormField(type='entry', label='Auto-save Interval (minutes)')
    ],
    FormsOptions(
        title="Application Settings",
        text="Configure your application preferences:",
        separator="|",
        show_header=True,
        width=550,
        height=550
    )
)

    if result.button == 'ok' and result.values:
        app_name, theme, language, font_size, default_action, autosave = result.values
        
        # Validation
        if autosave and not autosave.isdigit():
            print("✗ Error: Auto-save interval must be a number", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*50)
        print("✓ SETTINGS SAVED")
        print("="*50)
        print(f"Application Name: {app_name}")
        print(f"Theme: {theme}")
        print(f"Language: {language}")
        print(f"Font Size: {font_size}")
        print(f"Default Action: {default_action}")
        print(f"Auto-save Interval: {autosave} minutes")
        print("="*50)
        print("\nSettings have been applied successfully!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Settings not saved")
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
