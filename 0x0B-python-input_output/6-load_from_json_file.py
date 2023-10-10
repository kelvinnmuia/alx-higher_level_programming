#!/usr/bin/python3
"""defines function to create object
from JSON representation form file"""


def load_from_json_file(filename):
    """ creates object from JSON representation in file"""
    import jsom
    with open(filename, 'r') as f:
        return json.load(f)
