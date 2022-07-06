#!/usr/bin/python3
"""Module read_file
Has one function, read_file
"""


def read_file(filename=""):
    """reads a text file and prints it to stdout. """
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        print(line, end="")
