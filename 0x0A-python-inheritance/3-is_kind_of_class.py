#!/usr/bin/python3
""" defines a function that returns True if the object is an instance
of or if object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """ returns true in an object is an
    instance of class that inherited from"""
    return (isinstance(obj, a_class))
