#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest
import pep8

from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """testing Rectangle class functions"""

    def test_rectangle_instantiation(self):
        """test instatiation of rectangle"""
        r1 = Rectangle(12, 43, 52, 22)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r1.height, 43)
        self.assertEqual(r1.x, 52)
        self.assertEqual(r1.y, 22)
        r2 = Rectangle(6, 54, 32, 40)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 54)
        self.assertEqual(r1.x, 32)
        self.assertEqual(r1.y, 40)

    def test_pep8(self):
        """test that code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
