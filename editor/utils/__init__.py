from editor.components import codetab
from editor.utils import os_utils


def get_or_create_tab(file_name):
    """
    Check whether an input file is already loaded as a code tab, or load it.

    :param file_name: The input file name to check or create.
    :return: The code tab corresponding to the input file.
    """
    if file_name in get_or_create_tab.cache.keys():
        return get_or_create_tab.cache[file_name]

    # Did not find tab, create it instead
    code_tab = codetab.CodeTab(file=file_name)
    # Add code tab to tabbed panel
    get_or_create_tab.cache[file_name] = code_tab
    return code_tab


# TODO: Move tab management to its own class
get_or_create_tab.cache = {}
