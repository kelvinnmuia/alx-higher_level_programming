#!/usr/bin/python3
"""defines function to return object from JSON"""


def from_json_string(my_str):
    """returns objects from JSON"""
    import json
    return json.loads(my_str)
