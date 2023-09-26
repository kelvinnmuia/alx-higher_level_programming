#!/usr/bin/python3
"""this an empty class to define square"""


class Square:
    """the class to define square"""
    def __init__(self, size=0):
        """initialize the object parameters

        Args:
        size(int): the size of the square objects
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
