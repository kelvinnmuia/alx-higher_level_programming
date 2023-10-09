#!/usr/bin/python3
""" defines function to check whether you can add attribute"""


def add_attribute(obj, name, value):
    """checks whether you can add attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
