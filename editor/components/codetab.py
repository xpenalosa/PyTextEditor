import os

from kivy.cache import Cache
from kivy.uix.codeinput import CodeInput
from kivy.uix.tabbedpanel import TabbedPanelHeader

from editor.components.dialogs.file_chooser_dialog import FileChooserDialog
from editor.utils import lexer_utils


class CodeTab(TabbedPanelHeader):

    @staticmethod
    def get_or_create(file_name):
        """
        Check whether an input file is already loaded as a code tab, or load it.

        :param file_name: The input file name to check or create.
        :return: The code tab corresponding to the input file.
        """
        code_tab = Cache.get("code_tabs", file_name)
        if code_tab is None:
            # Did not find tab, create it instead
            code_tab = CodeTab(file=file_name)
            Cache.append("code_tabs", key=file_name, obj=code_tab)
        return code_tab

    def __init__(self, **kwargs):
        # Extract file from arguments
        text_file = kwargs.pop("file", None)
        super(CodeTab, self).__init__(**kwargs)

        # Initialize code input area
        self.code_input = CodeInput()
        # Assign file to hold the contents when saving or loading
        self.full_path = text_file
        if text_file is not None:
            # Parse file argument
            file_name = text_file.split(os.sep)[-1]
            # Populate CodeInput contents with file
            with open(text_file, 'r') as f:
                self.code_input.text = f.read()
            # Set tab name
            self.set_tab_name(file_name)
            # Mark as already saved
            self.is_unsaved = False
        else:
            # Assign temporal name
            self.set_tab_name("*new_file")
            # Mark as unsaved
            self.is_unsaved = True
        # Bind to text changed event
        self.code_input.bind(text=self._text_changed)
        # Assign code input to content for display
        self.content = self.code_input

    def set_tab_name(self, name: str):
        """
        Update the display name of the tab.

        This method also updates the tab lexer based on the filename extension.

        :param name: The new name to display.
        """
        # Update tab text
        self.text = name
        # Find appropriate lexer
        self.code_input.lexer = lexer_utils.get_code_lexer_for_filename(name)

    def set_full_path(self, path: str):
        """
        Assign the code input contents to a file designed by a path.

        :param path: The path to the file to assign the contents to.
        """
        self.full_path = path
        self.save_contents()
        # Update tab name and lexer
        file_name = path.split(os.sep)[-1]
        self.set_tab_name(file_name)

    def save_contents(self):
        """
        Store the contents of the CodeInput into the assigned file.

        If there is no file asssigned, a dialog is created to select the output
        file.
        """
        if self.full_path is None:
            dialog = FileChooserDialog(size_hint=(0.75, 0.75))
            dialog.set_callback(self.set_full_path)
            dialog.open()
        else:
            # Store contents to file
            with open(self.full_path, 'w') as f:
                f.write(self.content.text)
            # Contents changed
            if self.is_unsaved:
                # Remove flag
                self.is_unsaved = False
                # Remove indicator from tab name
                self.text = self.text.lstrip("*")

    def _text_changed(self, instance, value):
        if not self.is_unsaved:
            self.is_unsaved = True
            self.text = f"*{self.text}"
