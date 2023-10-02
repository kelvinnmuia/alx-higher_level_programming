#!/usr/bin/python3
"""defines a class rectangle"""
class Rectangle:
    """creates a class rectangle with attributes"""
    

    number_of_instances = 0
    print_symbol = "#"


    def __init__(self, width=0, height=0):
        """instantiates class rectangle with optional width/height attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter method for width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """setter method for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """getter method for the height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """setter method for the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

    def area(self):
        """public instance method to compute and return area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """public instance method to compute and return perimeter of a rectangle"""
        if self.width == 0 or self.width == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        rc_str = ""
        for _ in range(self.height):
            rc_str += str(self.print_symbol) * self.width + "\n"
        return rc_str[:-1]

    def __repr__(self):
        rc_str = "Rectangle(%s, %s)" % (self.width, self.height)
        return (rc_str)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not rect_1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not rect_2:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return(rect_1)
