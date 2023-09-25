#!/usr/bin/python3
"""exception for a function that divides two integers:

arguments:
    a: the dividend
    b: the divisor

Return: returns the quotient
"""


def safe_print_diviion(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
