#!/usr/bin/python3
""" defines function that returns true when the
object is exactly the same as the specified class"""


def is_same_class(obj, a_class):
    """ returns True when object is exactly
    the same as the specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
