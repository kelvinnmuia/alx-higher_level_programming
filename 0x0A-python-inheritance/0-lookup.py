#!/usr/bin/python3
""" defines a function that returns list of object methods and attributes"""


def lookup(obj):
    """ returns list of available object attributes """
    return (dir(obj))
