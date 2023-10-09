#!/usr/bin/python3
""" defines class that rebels integer class"""


class MyInt(int):
    """ rebels the the integer class with == and !="""
    def __eq__(self, other):
        """ returns ne when eq is called"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ returns eq when ne is called"""
        return super().__eq__(other)
