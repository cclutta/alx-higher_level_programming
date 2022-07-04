#!/usr/bin/python3
"""
is_kind_of_class module

Contains one function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """True if the object is inherited from. """
    return isinstance(obj, a_class)
