#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add two integers or floats and return the result as an integer

    Args:
        a (int or float): The first number
        b (int or float): Optional; The second number (defalt is 98)

    Returns:
        int: The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    #check whether a is not an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    #check whether b is not an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    #cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    #compute the sum and return the result as an integer
    return int(a + b)

