#!/usr/bin/python3
""" defines the rectangle class that inherits
BaseGeometry with print() and str()"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits BaseGeometry with print() and str()"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height

    def __str__(self):
        """ string represantation of rectangle"""
        str_rp = "[Rectangle] " + str(self._width) + "/" + str(self._height)
        return str_rp

    def area(self):
        return (self._width * self._height)
