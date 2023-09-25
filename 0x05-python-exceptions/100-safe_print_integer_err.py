#!/usr/bin/python3
"""exception and stderr for a function that prints integer values:

arguments:
    value: the integer to print

Return: returns the integer
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as e:
        import sys
        sys.stderr.write("Exception: {}".format(e))
        return False
