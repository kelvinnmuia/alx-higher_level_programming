#!/usr/bin/python3
"""creates class Square with
private attribute size position and public methods"""



class Square:
    """defines class with a private attribute size
    position and public methods"""


    def __init__(self, size=0, position=(0, 0)):
        """initializes size and position attributes to 0"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter method for size attribute"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """setter method for size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter method for position attribute"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """setter method for position attribute"""
        validate = 0
        while 1:
            if type(value) is not tuple or len(value) is not 2:
                validate += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                validate += 1
                break
            if value[0] < 0 or value[1] < 0:
                validate += 1
            break
        if validate is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """public instance method to calculate area of square"""
        return(self.__size * self.__size)

    def my_print(self):
        """public instance method to print square using #"""
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def my_print_string(self):
        """formats strings returned by my_print method"""
        sq_str = ""
        if self.__size > 0:
            for y in range(self.__position[1]):
                sq_str = sq_str + "\n"
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    sq_str = sq_str + " "
                for column in range(self.__size):
                    sq_str = sq_str + "#"
                if row is not (self.__size - 1):
                    sq_str = sq_str + "\n"
        return sq_str

    def __repr__(self):
        """returns string representing the square"""
        return (self.my_print_string())
