#!/usr/bin/python3
"""exception for a function that prints list elements:

arguments:
    my_list: the list
    x: the number of elements to print

Return: returns the lists elements
"""
def safe_print_list(mylist=[], x=0):
    result = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end="")
            result += 1
        except IndexError:
            break
        print("")
        return (result)

