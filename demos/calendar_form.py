#!/usr/bin/env python3
"""Demo: Calendar Form (Event Scheduler)"""

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
        FormField(type='entry', label='Event Name'),
        FormField(type='calendar', label='Event Date'),
        FormField(type='entry', label='Location'),
        FormField(type='multiline', label='Description')
    ],
    FormsOptions(
        title="Schedule Event",
        text="Enter event details:",
        separator="|",
        forms_date_format="%Y-%m-%d",
        width=550,
        height=600
    )
)

    if result.button == 'ok' and result.values:
        event_name, event_date, location, description = result.values
        
        # Validation
        if not event_name or not event_date:
            print("✗ Error: Event name and date are required", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*50)
        print("✓ EVENT SCHEDULED")
        print("="*50)
        print(f"Event: {event_name}")
        print(f"Date: {event_date}")
        print(f"Location: {location}")
        print(f"Description: {description}")
        print("="*50)
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Event scheduling cancelled")
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
