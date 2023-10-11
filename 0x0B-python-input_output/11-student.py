#!/usr/bin/python3
"""defines the Student class"""


class Student():
    """class for defining student"""

    def __init__(self, first_name, last_name, age):
        """instantiates the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary description for JSON serialization"""
        if type(attrs) is list:
            new_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all the attributes of the student class"""
        for k, v in json.items():
            setattr(self, k, v)
