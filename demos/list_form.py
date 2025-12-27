#!/usr/bin/env python3
"""Demo: List Form (Travel Booking)"""

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
        FormField(type='entry', label='Traveler Name'),
        FormField(
            type='combo',
            label='Destination',
            values=['Paris, France', 'Tokyo, Japan', 'New York, USA', 'London, UK', 'Dubai, UAE', 'Sydney, Australia']
        ),
        FormField(type='calendar', label='Departure Date'),
        FormField(
            type='combo',
            label='Class',
            values=['Economy', 'Premium Economy', 'Business', 'First Class']
        )
    ],
    FormsOptions(
        title="Flight Booking",
        text="Book your flight:",
        separator="|",
        forms_date_format="%Y-%m-%d",
        show_header=True,
        width=550,
        height=550
    )
)

    if result.button == 'ok' and result.values:
        name, destination, date, travel_class = result.values
        
        # Validation
        if not name or not destination or not date:
            print("✗ Error: Name, destination, and date are required", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*50)
        print("✓ FLIGHT BOOKING CONFIRMATION")
        print("="*50)
        print(f"Passenger: {name}")
        print(f"Destination: {destination}")
        print(f"Departure: {date}")
        print(f"Class: {travel_class}")
        print("="*50)
        print("\nBooking submitted successfully!")
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Booking cancelled")
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
