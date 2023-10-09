#!/usr/bin/python3
""" defines the BaseGeometry class that has public instance
method for area, pblic instance method for integer validation"""


class BaseGeometry:
    """"The BaseGeometry class with public
    instance method for area, integer validation"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
