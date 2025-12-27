#!/usr/bin/env python3
"""
Python Zenity Wrapper
A comprehensive Python wrapper for Zenity dialogs, making it easy to create
native desktop dialogs in your applications.
"""

import subprocess
import os
from typing import Optional, List, Any, Union, Literal
from dataclasses import dataclass


@dataclass
class CommonOptions:
    """Common options for all dialog types."""
    title: Optional[str] = None
    width: Optional[int] = None
    height: Optional[int] = None
    timeout: Optional[int] = None
    ok_label: Optional[str] = None
    cancel_label: Optional[str] = None
    extra_button: Optional[str] = None
    modal_hint: bool = False
    attach_parent: Optional[int] = None


@dataclass
class InfoOptions(CommonOptions):
    """Options for info, warning, and error dialogs."""
    no_wrap: bool = False
    no_markup: bool = False
    ellipsize: bool = False
    icon_name: Optional[str] = None


@dataclass
class QuestionOptions(CommonOptions):
    """Options for question dialogs."""
    default_cancel: bool = False
    no_wrap: bool = False
    no_markup: bool = False
    ellipsize: bool = False


@dataclass
class EntryOptions(CommonOptions):
    """Options for entry dialogs."""
    entry_text: Optional[str] = None
    hide_text: bool = False


@dataclass
class PasswordOptions(CommonOptions):
    """Options for password dialogs."""
    username: bool = False


@dataclass
class ScaleOptions(CommonOptions):
    """Options for scale/slider dialogs."""
    value: Optional[int] = None
    min_value: Optional[int] = None
    max_value: Optional[int] = None
    step: Optional[int] = None
    hide_value: bool = False
    print_partial: bool = False


@dataclass
class CalendarOptions(CommonOptions):
    """Options for calendar dialogs."""
    day: Optional[int] = None
    month: Optional[int] = None
    year: Optional[int] = None
    date_format: str = "%Y-%m-%d"


@dataclass
class ListOptions(CommonOptions):
    """Options for list dialogs."""
    checklist: bool = False
    radiolist: bool = False
    multiple: bool = False
    editable: bool = False
    separator: str = "|"
    print_column: Optional[int] = None
    hide_column: Optional[int] = None
    hide_header: bool = False


@dataclass
class ColorSelectionOptions(CommonOptions):
    """Options for color selection dialogs."""
    color: Optional[str] = None
    show_palette: bool = False


@dataclass
class FileSelectionOptions(CommonOptions):
    """Options for file selection dialogs."""
    multiple: bool = False
    directory: bool = False
    save: bool = False
    separator: str = "|"
    filename: Optional[str] = None
    confirm_overwrite: bool = False


@dataclass
class ProgressOptions(CommonOptions):
    """Options for progress dialogs."""
    percentage: Optional[int] = None
    pulsate: bool = False
    auto_close: bool = False
    auto_kill: bool = False
    no_cancel: bool = False
    time_remaining: bool = False


@dataclass
class FormField:
    """Base class for form fields."""
    type: Literal['entry', 'password', 'multiline', 'calendar', 'list', 'combo']
    label: str
    value: Optional[str] = None
    values: Optional[List[str]] = None
    header: Optional[str] = None
    column_values: Optional[List[str]] = None


@dataclass
class FormsOptions(CommonOptions):
    """Options for forms dialogs."""
    text: Optional[str] = None
    separator: str = "|"
    forms_date_format: Optional[str] = None
    show_header: bool = False


@dataclass
class FormsResult:
    """Result from forms dialog."""
    button: Literal['ok', 'cancel', 'extra']
    values: Optional[List[str]] = None


@dataclass
class TextOptions(CommonOptions):
    """Options for text dialogs."""
    filename: Optional[str] = None
    editable: bool = False
    font_name: Optional[str] = None
    checkbox: Optional[str] = None
    html_mode: bool = False
    url: Optional[str] = None
    auto_scroll: bool = False


class Zenity:
    """
    A comprehensive Python wrapper for Zenity dialogs.
    
    Provides easy-to-use methods for creating various types of native dialogs
    including message dialogs, input dialogs, file selectors, and more.
    """
    
    def __init__(self):
        """Initialize the Zenity wrapper."""
        # Set environment variables to prevent GTK4 crashes on macOS
        self.env = os.environ.copy()
        self.env['GSETTINGS_BACKEND'] = 'memory'
        self.env['GSETTINGS_SCHEMA_DIR'] = '/dev/null'
        self.env['G_MESSAGES_DEBUG'] = ''
    
    @staticmethod
    def _sanitize_input(value: str) -> str:
        """Sanitize input to prevent command injection."""
        # Zenity handles most escaping, but we validate for safety
        if not isinstance(value, str):
            value = str(value)
        # Remove null bytes that could cause issues
        return value.replace('\0', '')
    
    def _add_common_options(self, args: List[str], options: CommonOptions) -> None:
        """Add common options to the arguments list."""
        if options.title:
            args.append(f'--title={options.title}')
        if options.width:
            args.append(f'--width={options.width}')
        if options.height:
            args.append(f'--height={options.height}')
        if options.timeout:
            args.append(f'--timeout={options.timeout}')
        if options.ok_label:
            args.append(f'--ok-label={options.ok_label}')
        if options.cancel_label:
            args.append(f'--cancel-label={options.cancel_label}')
        if options.extra_button:
            args.append(f'--extra-button={options.extra_button}')
        if options.modal_hint:
            args.append('--modal')
        if options.attach_parent:
            args.append(f'--attach={options.attach_parent}')
    
    def _run(self, args: List[str]) -> str:
        """Run a Zenity command and return the output."""
        try:
            result = subprocess.run(
                ['zenity'] + args,
                capture_output=True,
                text=True,
                env=self.env,
                check=False
            )
        except FileNotFoundError:
            raise RuntimeError("Zenity is not installed. Please install it first.")
        except Exception as e:
            raise RuntimeError(f"Failed to run zenity: {str(e)}")

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            raise subprocess.CalledProcessError(result.returncode, args, result.stdout, result.stderr)
    
    def _run_with_exit_code(self, args: List[str]) -> tuple[str, str, int]:
        """Run a Zenity command and return output, stderr, and exit code."""
        try:
            result = subprocess.run(
                ['zenity'] + args,
                capture_output=True,
                text=True,
                env=self.env,
                check=False
            )
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        except FileNotFoundError:
            raise RuntimeError("Zenity is not installed. Please install it first.")
        except Exception as e:
            raise RuntimeError(f"Failed to run zenity: {str(e)}")
    
    def _run_with_input(self, args: List[str], input_text: str) -> str:
        """Run a Zenity command with input piped to stdin."""
        try:
            result = subprocess.run(
                ['zenity'] + args,
                input=input_text,
                capture_output=True,
                text=True,
                env=self.env,
                check=False
            )
        except FileNotFoundError:
            raise RuntimeError("Zenity is not installed. Please install it first.")
        except Exception as e:
            raise RuntimeError(f"Failed to run zenity: {str(e)}")

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            raise subprocess.CalledProcessError(result.returncode, args, result.stdout, result.stderr)
    
    # Message Dialogs
    
    def info(self, message: str, options: Optional[InfoOptions] = None) -> None:
        """Display an information dialog."""
        if options is None:
            options = InfoOptions()
        
        message = self._sanitize_input(message)
        args = ['--info', f'--text={message}']
        self._add_common_options(args, options)
        
        if options.no_wrap:
            args.append('--no-wrap')
        if options.no_markup:
            args.append('--no-markup')
        if options.ellipsize:
            args.append('--ellipsize')
        if options.icon_name:
            args.append(f'--icon-name={options.icon_name}')
        
        try:
            self._run(args)
        except subprocess.CalledProcessError:
            # Info dialogs don't need to throw
            pass
    
    def warning(self, message: str, options: Optional[InfoOptions] = None) -> None:
        """Display a warning dialog."""
        if options is None:
            options = InfoOptions()
        
        message = self._sanitize_input(message)
        args = ['--warning', f'--text={message}']
        self._add_common_options(args, options)
        
        if options.no_wrap:
            args.append('--no-wrap')
        if options.no_markup:
            args.append('--no-markup')
        if options.ellipsize:
            args.append('--ellipsize')
        if options.icon_name:
            args.append(f'--icon-name={options.icon_name}')
        
        try:
            self._run(args)
        except subprocess.CalledProcessError:
            # Warning dialogs don't need to throw
            pass
    
    def error(self, message: str, options: Optional[InfoOptions] = None) -> None:
        """Display an error dialog."""
        if options is None:
            options = InfoOptions()
        
        message = self._sanitize_input(message)
        args = ['--error', f'--text={message}']
        self._add_common_options(args, options)
        
        if options.no_wrap:
            args.append('--no-wrap')
        if options.no_markup:
            args.append('--no-markup')
        if options.ellipsize:
            args.append('--ellipsize')
        if options.icon_name:
            args.append(f'--icon-name={options.icon_name}')
        
        try:
            self._run(args)
        except subprocess.CalledProcessError:
            # Error dialogs don't need to throw
            pass
    
    def question(self, message: str, options: Optional[QuestionOptions] = None) -> bool:
        """
        Display a question dialog with OK/Cancel buttons.
        Returns True if OK clicked, False if cancelled.
        """
        if options is None:
            options = QuestionOptions()
        
        message = self._sanitize_input(message)
        args = ['--question', f'--text={message}']
        self._add_common_options(args, options)
        
        if options.default_cancel:
            args.append('--default-cancel')
        if options.no_wrap:
            args.append('--no-wrap')
        if options.no_markup:
            args.append('--no-markup')
        if options.ellipsize:
            args.append('--ellipsize')
        
        try:
            self._run(args)
            return True  # User clicked Yes/OK
        except subprocess.CalledProcessError as e:
            # Exit code 1 means user clicked No/Cancel
            if e.returncode in (1, 5):
                return False
            raise e
    
    # Input Dialogs
    
    def entry(self, text: str, options: Optional[EntryOptions] = None) -> Optional[str]:
        """Display a text entry dialog. Returns the entered text or None if cancelled."""
        if options is None:
            options = EntryOptions()
        
        args = ['--entry']
        if text:
            args.append(f'--text={text}')
        if options.entry_text:
            args.append(f'--entry-text={options.entry_text}')
        if options.hide_text:
            args.append('--hide-text')
        
        self._add_common_options(args, options)
        
        try:
            return self._run(args)
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    def password(self, options: Optional[PasswordOptions] = None) -> Optional[str]:
        """
        Display a password entry dialog.
        Returns the password, or 'username|password' if username option is enabled.
        Returns None if cancelled.
        """
        if options is None:
            options = PasswordOptions()
        
        args = ['--password']
        if options.username:
            args.append('--username')
        
        self._add_common_options(args, options)
        
        try:
            return self._run(args)
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    def scale(self, text: str, options: Optional[ScaleOptions] = None) -> Optional[int]:
        """Display a slider/scale dialog. Returns the selected number or None if cancelled."""
        if options is None:
            options = ScaleOptions()
        
        args = ['--scale']
        if text:
            args.append(f'--text={text}')
        if options.value is not None:
            args.append(f'--value={options.value}')
        if options.min_value is not None:
            args.append(f'--min-value={options.min_value}')
        if options.max_value is not None:
            args.append(f'--max-value={options.max_value}')
        if options.step is not None:
            args.append(f'--step={options.step}')
        if options.print_partial:
            args.append('--print-partial')
        if options.hide_value:
            args.append('--hide-value')
        
        self._add_common_options(args, options)
        
        try:
            result = self._run(args)
            return int(result) if result else None
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    def calendar(self, text: str, options: Optional[CalendarOptions] = None) -> Optional[str]:
        """Display a calendar date picker. Returns the selected date or None if cancelled."""
        if options is None:
            options = CalendarOptions()
        
        args = ['--calendar']
        if text:
            args.append(f'--text={text}')
        if options.day:
            args.append(f'--day={options.day}')
        if options.month:
            args.append(f'--month={options.month}')
        if options.year:
            args.append(f'--year={options.year}')
        if options.date_format:
            args.append(f'--date-format={options.date_format}')
        
        self._add_common_options(args, options)
        
        try:
            return self._run(args)
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    # Selection Dialogs
    
    def list(
        self,
        text: str,
        columns: List[str],
        data: List[List[Any]],
        options: Optional[ListOptions] = None
    ) -> Optional[Union[str, List[str]]]:
        """
        Display a list selection dialog.
        Returns selected value(s) or None if cancelled.
        """
        if options is None:
            options = ListOptions()
        
        args = ['--list']
        
        if text:
            args.append(f'--text={text}')
        if options.checklist:
            args.append('--checklist')
        if options.radiolist:
            args.append('--radiolist')
        if options.multiple:
            args.append('--multiple')
        if options.editable:
            args.append('--editable')
        if options.separator:
            args.append(f'--separator={options.separator}')
        if options.print_column is not None:
            args.append(f'--print-column={options.print_column}')
        if options.hide_column is not None:
            args.append(f'--hide-column={options.hide_column}')
        if options.hide_header:
            args.append('--hide-header')
        
        self._add_common_options(args, options)
        
        # Add columns
        for col in columns:
            args.append(f'--column={col}')
        
        # Add data
        for row in data:
            for item in row:
                args.append(str(item))
        
        try:
            result = self._run(args)
            if result and options.multiple and options.separator:
                return result.split(options.separator)
            return result
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    def color_selection(self, options: Optional[ColorSelectionOptions] = None) -> Optional[str]:
        """
        Display a color picker dialog.
        Returns selected color in rgb format or None if cancelled.
        
        Note: Does not work on macOS due to Zenity GTK limitations.
        """
        if options is None:
            options = ColorSelectionOptions()
        
        args = ['--color-selection']
        
        if options.color:
            color = options.color
            # Convert hex to rgb format if needed
            if color.startswith('#'):
                hex_color = color[1:]
                # Convert 8-bit (0-255) to 16-bit (0-65535) by multiplying by 257
                r = int(hex_color[0:2], 16) * 257
                g = int(hex_color[2:4], 16) * 257
                b = int(hex_color[4:6], 16) * 257
                color = f'rgb({r},{g},{b})'
            args.append(f'--color={color}')
        
        if options.show_palette:
            args.append('--show-palette')
        
        self._add_common_options(args, options)
        
        try:
            return self._run(args)
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    # File Dialogs
    
    def file_selection(
        self,
        options: Optional[FileSelectionOptions] = None
    ) -> Optional[Union[str, List[str]]]:
        """
        Display a file or directory selection dialog.
        Returns file path(s) or None if cancelled.
        """
        if options is None:
            options = FileSelectionOptions()
        
        args = ['--file-selection']
        
        if options.multiple:
            args.append('--multiple')
        if options.directory:
            args.append('--directory')
        if options.save:
            args.append('--save')
        if options.filename:
            args.append(f'--filename={options.filename}')
        if options.confirm_overwrite:
            args.append('--confirm-overwrite')
        if options.separator:
            args.append(f'--separator={options.separator}')
        
        self._add_common_options(args, options)
        
        try:
            result = self._run(args)
            if result and options.multiple and options.separator:
                return result.split(options.separator)
            return result
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
    
    # Progress Dialogs
    
    def progress(
        self,
        text: str,
        options: Optional[ProgressOptions] = None
    ) -> subprocess.Popen:
        """
        Display a progress dialog.
        Returns a Popen object for controlling the progress.
        
        Usage:
            proc = zenity.progress("Loading...", ProgressOptions(percentage=0, auto_close=True))
            proc.stdin.write("50\\n".encode())  # Update to 50%
            proc.stdin.write("# Processing...\\n".encode())  # Update message
            proc.stdin.close()  # Close when done
            proc.wait()
        """
        if options is None:
            options = ProgressOptions()
        
        args = ['--progress']
        
        if text:
            args.append(f'--text={text}')
        if options.percentage is not None:
            args.append(f'--percentage={options.percentage}')
        if options.auto_close:
            args.append('--auto-close')
        if options.auto_kill:
            args.append('--auto-kill')
        if options.pulsate:
            args.append('--pulsate')
        if options.no_cancel:
            args.append('--no-cancel')
        if options.time_remaining:
            args.append('--time-remaining')
        
        self._add_common_options(args, options)
        
        try:
            proc = subprocess.Popen(
                ['zenity'] + args,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                env=self.env,
                text=True
            )
            return proc
        except Exception as e:
            raise RuntimeError(f"Failed to create progress dialog: {str(e)}")
    
    def update_progress(
        self,
        process: subprocess.Popen,
        percentage: int,
        text: str = ''
    ) -> None:
        """Helper method to update a progress dialog."""
        if process.stdin:
            process.stdin.write(f'{percentage}\n')
            if text:
                process.stdin.write(f'# {text}\n')
            process.stdin.flush()
    
    # Advanced Dialogs
    
    def forms(
        self,
        fields: List[FormField],
        options: Optional[FormsOptions] = None
    ) -> FormsResult:
        """
        Display a multi-field form dialog.
        Returns FormsResult with button type and values.
        """
        if options is None:
            options = FormsOptions()
        
        args = ['--forms']
        
        if options.text:
            args.append(f'--text={options.text}')
        if options.separator:
            args.append(f'--separator={options.separator}')
        if options.forms_date_format:
            args.append(f'--forms-date-format={options.forms_date_format}')
        if options.show_header:
            args.append('--show-header')
        
        self._add_common_options(args, options)
        
        # Add form fields
        for field in fields:
            if field.type == 'entry':
                args.append(f'--add-entry={field.label}')
            elif field.type == 'password':
                args.append(f'--add-password={field.label}')
            elif field.type == 'multiline':
                args.append(f'--add-multiline-entry={field.label}')
            elif field.type == 'calendar':
                args.append(f'--add-calendar={field.label}')
            elif field.type == 'list':
                args.append(f'--add-list={field.label}')
                if field.header:
                    args.append(f'--list-header={field.header}')
                if field.values:
                    args.append(f'--list-values={"|".join(field.values)}')
                if field.column_values:
                    for val in field.column_values:
                        args.append(f'--column-values={val}')
            elif field.type == 'combo':
                args.append(f'--add-combo={field.label}')
                if field.values:
                    args.append(f'--combo-values={"|".join(field.values)}')
        
        result, stderr, exit_code = self._run_with_exit_code(args)
        separator = options.separator or '|'
        
        if exit_code == 0:
            # OK button clicked
            return FormsResult(button='ok', values=result.split(separator) if result else [])
        elif exit_code == 1:
            # Check if extra button was clicked
            if options.extra_button and result == options.extra_button:
                return FormsResult(button='extra', values=None)
            else:
                # User cancelled
                return FormsResult(button='cancel', values=None)
        elif exit_code == 5:
            # Timeout
            return FormsResult(button='cancel', values=None)
        else:
            # Error occurred
            raise subprocess.CalledProcessError(exit_code, args, result, stderr)

    
    def text(
        self,
        message: str,
        options: Optional[TextOptions] = None
    ) -> Optional[str]:
        """
        Display a text information dialog with optional editing.
        Returns the (possibly edited) text or None if cancelled.
        """
        if options is None:
            options = TextOptions()
        
        args = ['--text-info']
        
        if options.filename:
            args.append(f'--filename={options.filename}')
        if options.editable:
            args.append('--editable')
        if options.html_mode:
            args.append('--html')
        if options.url:
            args.append(f'--url={options.url}')
        if options.font_name:
            args.append(f'--font={options.font_name}')
        if options.checkbox:
            args.append(f'--checkbox={options.checkbox}')
        if options.auto_scroll:
            args.append('--auto-scroll')
        
        self._add_common_options(args, options)
        
        try:
            return self._run_with_input(args, message)
        except subprocess.CalledProcessError as e:
            if e.returncode in (1, 5):
                return None
            raise e
