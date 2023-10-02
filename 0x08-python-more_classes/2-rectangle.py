#!/usr/bin/python3
"""defines a class rectangle"""
class Rectangle:
    """creates a class rectangle with attributes"""
    def __init__(self, width=0, height=0):
        """instantiates class rectangle with optional width/height attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """getter method for the height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """public instance method to compute and return area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """public instance method to compute and return perimeter of a rectangle"""
        if self.width == 0 or self.width == 0:
            return 0
        return (2 * (self.width + self.height))

