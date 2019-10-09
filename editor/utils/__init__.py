from kivy.extras.highlight import KivyLexer
from kivy.uix.codeinput import CodeInput
from kivy.uix.tabbedpanel import TabbedPanelHeader

from pygments.lexers import get_lexer_for_filename
from pygments.util import ClassNotFound
from pygments.lexers.special import TextLexer

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
    code_input.lexer = get_code_lexer_for_filename(file_name)

    # Add new CodeInput object to the tabbed pane
    th = TabbedPanelHeader(text=file_name)
    th.content = code_input
    th.full_path = file_path
    return th


def get_code_lexer_for_filename(file_name):
    """
    Get a lexer that can highlight the contents of a file type.

    Select a pygments lexer with the utility function get_lexer_for_filename.
    If no such lexer exists, check if we opened a KivyLang file (.kv), Otherwise
    return a dummy lexer without highlighting.

    :param file_name: The name of the file to highlight.
    :return: An adequate lexer for the file, or a plain lexer if there are none
    available.
    """
    try:
        lexer = get_lexer_for_filename(file_name)
    except ClassNotFound:
        if file_name.split('.')[-1] == "kv":
            lexer = KivyLexer()
        else:
            lexer = TextLexer()
    return lexer


def store_code_tab(code_tab):
    """
    Store the contents of a code tab to disk.

    :param code_tab: The code tab from which to read the contents.
    """
    with open(code_tab.full_path, 'w') as f:
        f.write(code_tab.content.text)


def get_or_create_tab(file_name):
    """
    Check whether an input file is already loaded as a code tab, or load it.

    :param file_name: The input file name to check or create.
    :return: The code tab corresponding to the input file.
    """
    if file_name in get_or_create_tab.cache.keys():
        return get_or_create_tab.cache[file_name]

    # Did not find tab, create it instead
    code_tab = code_tab_from_file(file_name)
    # Add code tab to tabbed panel
    get_or_create_tab.cache[file_name] = code_tab
    return code_tab


# TODO: Move tab management to its own class
get_or_create_tab.cache = {}
