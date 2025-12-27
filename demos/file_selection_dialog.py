#!/usr/bin/env python3
"""Demo: File Selection Dialogs"""

import sys
sys.path.insert(0, '..')

try:
    from zenity_wrapper import Zenity, FileSelectionOptions, QuestionOptions
except ImportError as e:
    print(f"Error: Failed to import zenity_wrapper: {e}", file=sys.stderr)
    sys.exit(1)

try:
    zenity = Zenity()

    print("Demo 1: Open single file")
    file_path = zenity.file_selection(
        FileSelectionOptions(title="Select a File")
    )
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected")

    # Ask if user wants to continue
    try:
        if not zenity.question("Continue to multiple file selection?", QuestionOptions(title="Continue?")):
            sys.exit(0)
    except:
        sys.exit(0)

    print("\nDemo 2: Open multiple files")
    files = zenity.file_selection(
        FileSelectionOptions(
            title="Select Multiple Files",
            multiple=True,
            separator="|"
        )
    )
    if files:
        print(f"Selected {len(files) if isinstance(files, list) else 1} file(s):")
        if isinstance(files, list):
            for f in files:
                print(f"  - {f}")
        else:
            print(f"  - {files}")
    else:
        print("No files selected")

    # Ask if user wants to continue
    try:
        if not zenity.question("Continue to directory selection?", QuestionOptions(title="Continue?")):
            sys.exit(0)
    except:
        sys.exit(0)

    print("\nDemo 3: Select directory")
    directory = zenity.file_selection(
        FileSelectionOptions(
            title="Select a Directory",
            directory=True
        )
    )
    if directory:
        print(f"Selected directory: {directory}")
    else:
        print("No directory selected")

    # Ask if user wants to continue
    try:
        if not zenity.question("Continue to save file dialog?", QuestionOptions(title="Continue?")):
            sys.exit(0)
    except:
        sys.exit(0)

    print("\nDemo 4: Save file")
    save_path = zenity.file_selection(
        FileSelectionOptions(
            title="Save File As",
            save=True,
            filename="document.txt",
            confirm_overwrite=True
        )
    )
    if save_path:
        print(f"✓ Save file to: {save_path}")
        sys.exit(0)
    else:
        print("✗ Save cancelled")
        sys.exit(1)
        
except FileNotFoundError:
    print("Error: Zenity is not installed. Install it with: brew install zenity", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
