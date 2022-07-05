#!/usr/bin/python3
""" Load from JSON file Module
Contains one function, load_from_json_file()
"""
import json


def load_from_json_file(filename):
    """ that creates an Object from a JSON file. """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return json.loads(lines)
