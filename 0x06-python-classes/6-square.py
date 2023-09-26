#!/usr/bin/python3
"""this an empty class to define square"""


class Square:
    """the class to define square"""
    def __init__(self, size=0):
        """initialize the object parameters

        Args:
        size(int): the size of the square objects
        """

        self.size = size  # Use the property setter to the size

        @property
        def size(self):
            return self.__size

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        @property
        def position(self):
            return self.__position

        @position.setter
        def position(self, value):
            if (
                    not isinstance(value, tuple)
                    or len(value) != 2
                    or not all(isinstance(x, int) for x in value)
                    or not all(x >= 0 for x in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value

    def area(self):
        """public instance method to return current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square with # symbol"""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.position[1]):
                print("")
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
