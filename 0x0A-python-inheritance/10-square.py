#!/usr/bin/python3
""" defines the square class that inherits
Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle class that inherits BaseGeometry with print() and str()"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def area(self):
        return (self._size ** 2)
