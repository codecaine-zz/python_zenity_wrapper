#!/usr/bin/env python3
"""Demo: Calendar Dialog (Date Picker)"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, CalendarOptions
    from datetime import datetime
except ImportError as e:
    print(f"Error: Failed to import required modules: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()
    
    # Get today's date
    today = datetime.now()
    
    date = zenity.calendar(
        "Select your birth date:",
        CalendarOptions(
            title="Date Picker",
            day=1,
            month=1,
            year=2000,
            date_format="%Y-%m-%d"
        )
    )

    if date:
        print(f"✓ Selected date: {date}")
        
        # Calculate age if valid date format
        try:
            birth_date = datetime.strptime(date, "%Y-%m-%d")
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            print(f"Age: {age} years old")
            sys.exit(0)
        except ValueError as e:
            print(f"Warning: Could not parse date: {e}")
            print(f"Date selected: {date}")
            sys.exit(0)
    else:
        print("✗ User cancelled")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
