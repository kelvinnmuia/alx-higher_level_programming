#!/usr/bin/python3
"""max_integer([..]) unittest"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """has functions for testing max_integer function"""

    def test_unordered(self):
        """Testing the function with unordered integers"""
        self.assertEqual(max_integer([5, 1, 3, 2]), 5)
        self.assertEqual(max_integer([3, 1, 2, 9]), 9)

    def test_ordered(self):
        """Testing the function with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty(self):
        """Testing the function with an empty list"""
        self.assertEqual(max_integer([]), None)
