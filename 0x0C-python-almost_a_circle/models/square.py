#!/usr/bin/python3
"""defines the Square class which inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class for the Square instances"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the Square instance"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter method for size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """setter for the private instance attribute size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """overrides the __str__ with new string format"""
        str_rp = "[Square] ({}) {}/{} - {}".format(
            str(self.id), str(self.x), str(self.y), str(self.size))
        return (str_rp)
