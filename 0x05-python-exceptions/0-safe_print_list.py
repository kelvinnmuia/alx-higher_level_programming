#!/usr/bin/python3
"""exception for a function that prints list elements:

arguments:
    my_list: the list
    x: the number of elements to print

Return: returns the lists elements
"""


def safe_print_list(my_list=[], x=0):
    counter = 0

    for i in range(x):
        try:
            print(my_list[i], end='')
            counter += 1
        except IndexError:
            break
    print("")
    return counter
