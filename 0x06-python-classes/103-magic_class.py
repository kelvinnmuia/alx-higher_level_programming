#!/usr/bin/python3
"""creating a MagicClass matching the bytecode provided by Alx."""

import math


class MagicClass:
    """defining the circle."""

    def __init__(self, radius=0):
        """Initializing the MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculate area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """calculate circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
