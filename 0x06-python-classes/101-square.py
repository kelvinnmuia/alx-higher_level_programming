#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        # Initialize size and position attributes
        self.size = size
        self.position = position

    @property
    def size(self):
        # Getter for size attribute
        return self.__size

    @size.setter
    def size(self, value):
        # Setter for size attribute with type and value checks
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        # Getter for position attribute
        return self.__position

    @position.setter
    def position(self, value):
        # Setter for position attribute with type and value checks
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(val, int) and val >= 0 for val in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        # Calculate and return the area of the square
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        # Print the square using size and position attributes
        for _ in range(self.__position[1]):
            print()  # Print empty lines based on the vertical position
        for _ in range(self.__size):
            # Print the square's rows with appropriate indentation and #
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        # Override the __str__ method to return the output of my_print
        return self.my_print()
