from kivy.uix.codeinput import CodeInput
from kivy.uix.tabbedpanel import TabbedPanelHeader

from pygments.lexers import get_lexer_for_filename
from pygments.util import ClassNotFound

import os


def code_tab_from_file(file_path):
    """
    Create a tab containing a CodeInput object from a specified file.

    The CodeInput object will be populated with the contents of the input file,
    and will be automatically applied (if possible) the syntax highlighting for
    the file format.

    :param file_path: The file to read.
    :return: The created code tab.
    """
    file_name = file_path.split(os.sep)[-1]
    code_input = CodeInput()
    with open(file_path, 'r') as f:
        code_input.text = f.read()
        try:
            new_lexer = get_lexer_for_filename(file_name)
        except ClassNotFound:
            print(f"No lexer for {file_name}!")
        else:
            code_input.lexer = new_lexer

    # Add new CodeInput object to the tabbed pane
    th = TabbedPanelHeader(text=file_name)
    th.content = code_input
    th.full_path = file_path
    return th


def store_code_tab(code_tab):
    """
    Store the contents of a code tab to disk.

    :param code_tab: The code tab from which to read the contents.
    """
    with open(code_tab.full_path, 'w') as f:
        f.write(code_tab.content.text)


def get_or_create_tab(tabbed_pane, file_name):
    """
    Check whether an input file is already loaded as a code tab, or load it.

    :param tabbed_pane: The tabbed pane containing all the loaded tabs.
    :param file_name: The input file name to check or create.
    :return: The code tab corresponding to the input file.
    """
    code_tab = None
    # Iterate over open tabs
    for open_tab in tabbed_pane.tab_list:
        if open_tab.full_path == file_name:
            # Tab's full path matches
            code_tab = open_tab
            break
    else:
        # Did not find tab, create it instead
        code_tab = code_tab_from_file(file_name)
        # Add code tab to tabbed panel
        tabbed_pane.add_widget(code_tab)
    return code_tab
