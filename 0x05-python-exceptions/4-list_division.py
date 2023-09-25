#!/usr/bin/python3
"""exception for a function that divides elements between two lists:

arguments:
    my_list_1: the first list
    my_list_2: the second list
    list_length: the number of list elements to divide

Return: returns a new list with the quotients of all the divisions
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(0, list_length):
        try:
            divs = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divs = 0
        except ZeroDivisionError:
            print("division by 0")
            divs = 0
        except IndexError:
            print("out of range")
            divs = 0
        finally:
            new_list.append(div)
    return new_list
