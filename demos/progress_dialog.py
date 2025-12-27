#!/usr/bin/env python3
"""Demo: Progress Dialogs"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, ProgressOptions, QuestionOptions
    import time
except ImportError as e:
    print(f"Error: Failed to import required modules: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()

    print("Demo 1: Percentage Progress")
    progress = zenity.progress(
        "Processing files...",
        ProgressOptions(
            title="Progress",
            percentage=0,
            auto_close=True
        )
    )

    for i in range(0, 101, 10):
        zenity.update_progress(progress, i, f"Processing... {i}%")
        time.sleep(0.3)

    if progress.stdin:
        progress.stdin.close()
    progress.wait()
    print("Progress complete!\n")

    # Ask if user wants to continue
    try:
        if not zenity.question("Continue to pulsating progress demo?", QuestionOptions(title="Continue?")):
            sys.exit(0)
    except:
        sys.exit(0)

    print("Demo 2: Pulsating Progress (indefinite)")
    progress2 = zenity.progress(
        "Please wait while we process your request...",
        ProgressOptions(
            title="Processing",
            pulsate=True,
            auto_close=True,
            no_cancel=True
        )
    )

    # Simulate some work
    time.sleep(3)

    # Complete the progress
    progress2.stdin.write("100\n")
    progress2.stdin.close()
    progress2.wait()
    print("✓ Processing complete!")
    sys.exit(0)
    
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
