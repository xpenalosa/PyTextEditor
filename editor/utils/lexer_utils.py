from kivy.extras.highlight import KivyLexer

from pygments.lexers import get_lexer_for_filename
from pygments.util import ClassNotFound
from pygments.lexers.special import TextLexer


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
