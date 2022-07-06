#!/usr/bin/python3
"""Module append_write
Has one function, append_write
"""


def append_write(filename="", text=""):
    """that appends a string at the end of a text file. """

    with open(filename, 'a') as f:
        return f.write(text)
