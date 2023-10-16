#!/usr/bin/python3
"""defines the Base class"""


class Base():
    """manages the id attribute in future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class nb_objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of the list of dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
