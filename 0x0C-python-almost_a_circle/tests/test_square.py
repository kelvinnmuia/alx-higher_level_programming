#!/usr/bin/python3
"""unittest for the Square class"""


import unittest
import pep8

from models.square import Square


class Test_Square(unittest.TestCase):
    """test instatiation of square"""
    
    def test_square_instantiation(self):
        """tests Square instantiation"""
        r1 = Square(10, 20, 30, 40)
        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 20)
        self.assertEqual(r1.y, 30)

    def test_pep8(self):
        """tests whether code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


