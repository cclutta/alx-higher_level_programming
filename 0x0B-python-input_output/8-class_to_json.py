#!/usr/bin/python3
""" Class to JSON module
One function, class_to_json
"""


def class_to_json(obj):
    """ Returns dict desc with simple data structure. """
    return obj.__dict__
