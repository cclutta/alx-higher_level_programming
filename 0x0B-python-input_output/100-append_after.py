#!/usr/bin/python3
"""Append after module
Contains one function, append_after()
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to afile after each line containing. """
    str = ""
    with open(filename, 'r') as f:
        for line in f:
            str += line
            if search_string in line:
                str += new_string
    with open(filename, 'w') as f:
        f.write(str)
