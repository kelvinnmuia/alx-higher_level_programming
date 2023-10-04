#!/usr/bin/python3
"""defines a function to print square pattern using #"""


def print_square(size):
    """prints square pattern of any given size using #"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#"*size, end="")
        print()
