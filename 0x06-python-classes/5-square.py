#!/usr/bin/python3
"""creates class Square with
private attribute size and public methods"""


class Square:
    """defines class with a private attribute size and public methods"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instance method to calculate area of square"""
        return(self.__size * self.__size)

    def my_print(self):
        """public instance method to print square using #"""
        if self.__size > 0:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
