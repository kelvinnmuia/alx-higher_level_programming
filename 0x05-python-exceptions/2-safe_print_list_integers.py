#!/usr/bin/python3
"""exception for a function that prints integers in a list:

arguments:
    my_list: the list
    x: the elements or integers to access

Return: returns the lists integers
"""


def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for i in range(x):
        try:
            element = my_list[i]

            if isinstance(element, int):
                print("{:d}".format(element), end=" ")
                counter += 1
        except IndexError:
            raise Exception("list index out of range")

    print("")

    return counter
