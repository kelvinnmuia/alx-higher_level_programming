#!/usr/bin/python3
"""defines the Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class for square instances"""

    def __init__(self, size, x=0, y=0, id=None):
    """instantiates the Square class"""
    super().__init__(size, size, x, y, id)
    self.size = size

    @property
    def size(self):
        """getter for the private instance attribute size"""
        return (self.width)

    @size.setter(self, value):
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
        """overides the __str__ method with new string format"""
        str_rp = "[Square] ({}) {}/{} - {}".format(
                str(self.id), str(self.x), str(self.y), str(self.width))
        return (str_rp)

    def update(self, *args, **kwargs):
        """assigns an argument to each Square attribute"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for kw in kwargs:
                if kw == "id":
                    self.id = (kwargs[kw])
                if kw == "size":
                    self.size(kwargs[kw)
                if kw == "x":
                    self.x = (kwargs[kw])
                if kw == "y":
                    self.y = (kwargs[kw])

    def to_dictionary(self):
        """returns dictionary representation of a Square"""
        dict_rp = {}
        dict_rp["id"] = self.id
        dict_rp["size"] = self.size
        dict_rp["x"] = self.x
        dict_rp["y"] = self.y
        return dict_rp
