#!/usr/bin/python3
"""creating a Square class that defines
    a square with new attributes"""


class Square:
    """representing the new square attributes"""
    def __init__(self, size=0):
        """ initializing the new square"""
        self.__size = size

    @property
    def size(self):
        """getter method for the new square size"""
        return(self.__size)

    @size.setter
    """setter method for the new square"""
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public method to calculate current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """public method to print the square using #"""
        if self.__size > 0:
            for y in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
