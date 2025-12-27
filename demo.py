#!/usr/bin/env python3
"""
Python Zenity Wrapper Demo Launcher
Interactive menu to select and run different Zenity demos
"""

from zenity_wrapper import Zenity, ListOptions, InfoOptions, QuestionOptions
import os
import sys
import subprocess
from pathlib import Path


def get_demo_files():
    """Get all demo Python files from the demos directory"""
    demos_dir = Path(__file__).parent / "demos"
    
    if not demos_dir.exists():
        return []
    
    # Get all .py files except __pycache__ and README
    demo_files = []
    for file in sorted(demos_dir.glob("*.py")):
        if file.name != "__init__.py":
            demo_files.append(file)
    
    return demo_files


def format_demo_name(filename):
    """Convert filename to a readable demo name"""
    # Remove .py extension and replace underscores with spaces
    if isinstance(filename, str):
        name = filename.replace(".py", "").replace("_", " ").title()
    else:
        name = filename.stem.replace("_", " ").title()
    return name


def get_demo_description(demo_path):
    """Extract description from demo file docstring"""
    try:
        with open(demo_path, 'r') as f:
            lines = f.readlines()
            # Look for docstring in first few lines
            for i, line in enumerate(lines[:10]):
                if '"""' in line or "'''" in line:
                    # Extract text after Demo: or just the docstring content
                    desc = line.split('"""')[1] if '"""' in line else line.split("'''")[1]
                    desc = desc.replace("Demo:", "").strip()
                    if desc:
                        return desc
            return "No description available"
    except:
        return "No description available"


def run_demo(demo_path):
    """Run a selected demo"""
    try:
        print(f"\n{'='*60}")
        print(f"Running: {demo_path.name}")
        print(f"{'='*60}\n")
        
        # Run the demo in a subprocess
        result = subprocess.run(
            [sys.executable, str(demo_path)],
            cwd=demo_path.parent
        )
        
        print(f"\n{'='*60}")
        print(f"Demo completed with exit code: {result.returncode}")
        print(f"{'='*60}\n")
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"Error running demo: {e}", file=sys.stderr)
        return False


def main():
    zenity = Zenity()
    
    print("=== Python Zenity Wrapper Demo Launcher ===\n")
    
    # Get available demos
    demo_files = get_demo_files()
    
    if not demo_files:
        zenity.error(
            "No demo files found in the demos directory!",
            InfoOptions(title="Error")
        )
        return
    
    print(f"Found {len(demo_files)} demos\n")
    
    # Main loop - keep showing menu until user cancels
    while True:
        # Prepare list data for Zenity
        columns = ["Demo Name", "Description"]
        rows = []
        
        for demo_file in demo_files:
            name = format_demo_name(demo_file.name)
            description = get_demo_description(demo_file)
            rows.append([name, description])
        
        # Show list dialog
        selection = zenity.list(
            "Select a demo to run:",
            columns,
            rows,
            ListOptions(
                title="Zenity Demo Launcher",
                width=800,
                height=600,
                print_column=1  # Return the demo name
            )
        )
        
        # Check if user cancelled
        if not selection:
            print("Demo launcher closed by user")
            break
        
        # Find the selected demo file
        selected_demo = None
        for demo_file in demo_files:
            if format_demo_name(demo_file.name) == selection:
                selected_demo = demo_file
                break
        
        if selected_demo:
            # Run the demo
            success = run_demo(selected_demo)
            
            # Ask if user wants to continue (regardless of outcome)
            # Exit code 1 might just mean user cancelled the demo, not an error
            try:
                # Use list instead of question because question might be flaky on macOS
                choice = zenity.list(
                    f"Demo '{selection}' finished.\n\nWould you like to run another demo?",
                    ["Option"],
                    [["Yes"], ["No"]],
                    ListOptions(
                        title="Demo Launcher",
                        height=250,
                        hide_header=True
                    )
                )
                if choice != "Yes":
                    break
            except subprocess.CalledProcessError as e:
                # Only break if it's a user cancellation (exit code 1) or timeout (5)
                if e.returncode in (1, 5):
                    break
                print(f"Error showing continue dialog: {e}", file=sys.stderr)
                break
            except Exception as e:
                print(f"Error showing continue dialog: {e}", file=sys.stderr)
                break
        else:
            zenity.warning(
                f"Could not find demo file for: {selection}",
                InfoOptions(title="Warning")
            )
    
    print("\n=== Demo Launcher Closed ===")


if __name__ == '__main__':
    main()
