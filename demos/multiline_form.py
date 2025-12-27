#!/usr/bin/env python3
"""Demo: Multiline Form (Blog Post Creator)"""

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
        FormField(type='entry', label='Post Title'),
        FormField(type='multiline', label='Content'),
        FormField(type='entry', label='Tags (comma-separated)')
    ],
    FormsOptions(
        title="Create Blog Post",
        text="Write your blog post below:",
        separator="||",
        width=600,
        height=800  # Larger height for multiline field
    )
)

    if result.button == 'ok' and result.values:
        title, content, tags = result.values
        
        # Validation
        if not title or not content:
            print("✗ Error: Title and content are required", file=sys.stderr)
            sys.exit(1)
        
        print("\n" + "="*60)
        print("✓ BLOG POST CREATED")
        print("="*60)
        print(f"\nTitle: {title}")
        print(f"\nContent:\n{content}")
        print(f"\nTags: {tags}")
        print("\n" + "="*60)
        sys.exit(0)
    elif result.button == 'cancel':
        print("✗ Post creation cancelled")
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
