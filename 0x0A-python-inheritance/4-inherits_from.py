#!/usr/bin/python3
"""
inherits_from module

Contains one function inherits_from
"""


def inherits_from(obj, a_class):
    """True if the object is inherited from. """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
