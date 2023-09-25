#!/usr/bin/python3
"""exception for a function that prints integer value:

arguments:
    Value: the value to print

Return: returns the integer value
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
