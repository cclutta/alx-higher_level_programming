#!/usr/bin/python3
"""
is_same_class module

Contains one function is_same_class
"""


def is_same_class(obj, a_class):
    """True if the object is inherited from. """
    return type(obj) is a_class
