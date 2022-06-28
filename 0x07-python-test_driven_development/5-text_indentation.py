#!/usr/bin/python3
"""
text_indentation module.

one function, text_indentation().
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :.
    Args:
        text (str): the text to print.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for i in range(len(text)):
        line += text[i]
        if text[i] in ".?:":
            print((line + '\n').lstrip(' '))
            line = ""
    print(line.lstrip(' '), end='')
