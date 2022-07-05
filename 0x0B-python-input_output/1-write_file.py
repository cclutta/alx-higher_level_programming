#!/usr/bin/python3
"""Module write_file
Has one function, write_file
"""


def write_file(filename="", text=""):
    """writes a string toa text file. """

    with open(filename, 'w') as f:
        return f.write(text)
