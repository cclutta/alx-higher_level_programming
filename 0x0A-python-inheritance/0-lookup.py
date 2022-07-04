#!/usr/bin/python3
"""
lookup module

Contains one function lookup
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
