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
