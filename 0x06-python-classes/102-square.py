#!/usr/bin/python3
"""create the new square class."""


class Square:
    """Define the new square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public method to calculate current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, altn):
        """equal to."""
        return self.area() == altn.area()

    def __ne__(self, altn):
        """not equal to."""
        return self.area() != altn.area()

    def __lt__(self, altn):
        """less than."""
        return self.area() < altn.area()

    def __le__(self, altn):
        """less than or equal to."""
        return self.area() <= altn.area()

    def __gt__(self, altn):
        """greater than."""
        return self.area() > altn.area()

    def __ge__(self, altn):
        """greater than or equal to."""
        return self.area() >= altn.area()
