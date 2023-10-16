#!/usr/bin/python3
"""unittest for the Base class"""


import unittest
import pep8

from models.base import Base


class TestBase(unittest.TestCase):
    """testing Base class functions"""

    def test_base_instatiation(self):
        """tests the initialization of id when None and int"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(50)
        self.assertEqual(b2.id, 50)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_pep8(self):
        """test whether code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
