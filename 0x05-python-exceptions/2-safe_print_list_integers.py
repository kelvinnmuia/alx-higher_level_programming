#!/usr/bin/python3
"""exception for a function that prints integers in a list:

arguments:
    my_list: the list
    x: the elements or integers to access

Return: returns the lists integers
"""


def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue

    print("")
    return counter
