# Python Zenity Wrapper

A comprehensive Python wrapper for Zenity dialogs, making it easy to create native desktop dialogs in your applications.

![Python Zenity Wrapper Demo](screenshot.png)

> **Note:** A Bun version of this library is available at [bun_zenity](https://github.com/codecaine-zz/bun_zenity).

## Installation

### Install the Python Package

```bash
# Install from PyPI (once published)
pip3 install python-zenity-wrapper

# Or install from source
git clone https://github.com/codecaine-zz/python_zenity_wrapper.git
cd python_zenity_wrapper
pip3 install -e .
```

### Install Zenity (Required)

This package requires Zenity to be installed on your system:

```bash
# macOS
brew install zenity

# Ubuntu/Debian
sudo apt-get install zenity

# Fedora
sudo dnf install zenity
```

## Project Structure

```
python_zenity_wrapper/
├── zenity_wrapper.py       # Main Zenity wrapper module
├── app.py                  # Simple usage example
├── example_multiline.py    # Multiline form example
└── demo.py                 # Comprehensive demo of all features
```

## Quick Start

### Basic Usage

```python
from zenity_wrapper import Zenity, InfoOptions

zenity = Zenity()
zenity.info("Hello, World!", InfoOptions(title="Greeting"))
```

### Simple Example (app.py)

Run the simple example:
```bash
python3 app.py
```

Shows basic info, question, and form dialogs.

### Multiline Form Example (example_multiline.py)

Run the multiline form example:
```bash
python3 example_multiline.py
```

Demonstrates creating a blog post form with multiline text area.

### Comprehensive Demo (demo.py)

Run the full demo:
```bash
python3 demo.py
```

Demonstrates:
- All message dialogs (info, warning, error, question)
- All input dialogs (entry, password, scale, calendar)
- All selection dialogs (list, checklist, radiolist, color picker)
- File selection dialogs
- Progress dialogs
- Advanced forms with all field types
- Security validation

## Usage Examples

### Message Dialogs

```python
from zenity_wrapper import Zenity, InfoOptions, QuestionOptions

zenity = Zenity()

# Info dialog
zenity.info("Operation completed!", InfoOptions(title="Success"))

# Question dialog
answer = zenity.question("Continue?", QuestionOptions(ok_label="Yes", cancel_label="No"))
if answer:
    print("User said yes")
```

### Form with All Field Types

```python
from zenity_wrapper import Zenity, FormField, FormsOptions

zenity = Zenity()

result = zenity.forms(
    [
        FormField(type='entry', label='Name'),
        FormField(type='password', label='Password'),
        FormField(type='multiline', label='Bio'),
        FormField(type='calendar', label='Birth Date'),
        FormField(type='combo', label='Gender', values=['Male', 'Female', 'Other']),
        FormField(type='list', label='Country', values=['USA', 'Canada', 'UK'])
    ],
    FormsOptions(
        title="Registration",
        text="Fill out the form",
        separator="||",
        width=600,
        height=700
    )
)

if result.button == 'ok' and result.values:
    print("Form submitted:", result.values)
```

### Multiline Form (Bun Zenity Style)

```python
from zenity_wrapper import Zenity, FormField, FormsOptions

zenity = Zenity()

result = zenity.forms(
    [
        FormField(type='entry', label='Title'),
        FormField(type='multiline', label='Description'),
        FormField(type='entry', label='Tags')
    ],
    FormsOptions(
        text="Create a Post",
        separator="||",
        width=600,
        height=800  # More height = more space for multiline field
    )
)

if result.button == 'ok' and result.values:
    title, description, tags = result.values
    print(f"Post: {title}\n{description}\nTags: {tags}")
```

### Progress Dialog

```python
from zenity_wrapper import Zenity, ProgressOptions
import time

zenity = Zenity()

progress = zenity.progress(
    "Processing...",
    ProgressOptions(percentage=0, auto_close=True)
)

for i in range(0, 101, 20):
    zenity.update_progress(progress, i, f"Step {i}%")
    time.sleep(0.5)

progress.stdin.close()
progress.wait()
```

## Available Dialog Types

### Message Dialogs
- `info()` - Information message
- `warning()` - Warning message
- `error()` - Error message
- `question()` - Yes/No question

### Input Dialogs
- `entry()` - Text input
- `password()` - Password input (hidden text)
- `scale()` - Slider/number picker
- `calendar()` - Date picker

### Selection Dialogs
- `list()` - List selection (single/multiple/checklist/radiolist)
- `color_selection()` - Color picker
- `file_selection()` - File/directory picker

### Progress Dialogs
- `progress()` - Progress bar with live updates

### Advanced Dialogs
- `forms()` - Multi-field forms
- `text()` - Text viewer/editor

## Form Field Types

All 6 form field types supported:

1. **`entry`** - Single-line text input
2. **`password`** - Hidden password input
3. **`multiline`** - Multi-line text area
4. **`calendar`** - Date picker
5. **`combo`** - Dropdown selection
6. **`list`** - List selection

## Security Features

✓ Input sanitization (null byte removal)  
✓ Safe subprocess calls (list-based arguments)  
✓ No shell=True usage (prevents shell injection)  
✓ Environment variable isolation  
✓ Proper error handling

## API Documentation

Import all classes from `zenity_wrapper`:

```python
from zenity_wrapper import (
    Zenity,
    # Options classes
    InfoOptions,
    QuestionOptions,
    EntryOptions,
    PasswordOptions,
    ScaleOptions,
    CalendarOptions,
    ListOptions,
    ColorSelectionOptions,
    FileSelectionOptions,
    ProgressOptions,
    FormsOptions,
    TextOptions,
    # Data classes
    FormField,
    FormsResult
)
```

## License

MIT

## Contributing

Contributions welcome! All dialogs should be tested with Zenity installed.
