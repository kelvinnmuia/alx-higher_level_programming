#!/usr/bin/python3
"""defines the Student class"""


class Student():
    """class for defining student"""

    def __init__(self, first_name, last_name, age):
        """instantiates the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary description for JSON serialization"""
        return self.__dict__
