#!/usr/bin/python3
""" Save to JSON file Module
Contains one function, save_to_json_file()
"""
import json


def save_to_json_file(my_obj, filename):
    """ that writes an Object to a text file using JSON. """
    jsonstring = json.dumps(my_obj)

    with open(filename, 'w') as f:
        return f.write(jsonstring)
