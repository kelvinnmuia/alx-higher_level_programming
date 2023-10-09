#!/usr/bin/python3
""" defines a class that inherits from list """


class MyList(list):
    """class that inherits from list and a public method sorted"""
    def print_sorted(self):
        print(sorted(self))
