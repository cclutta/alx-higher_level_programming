#!/usr/bin/python3
"""
add_attribute module
contains one function, add_attribute()
"""


def add_attribute(obj, name, value):
    """ adds a new attribute to an object """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
