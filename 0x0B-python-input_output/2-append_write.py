#!/usr/bin/python3
""" defines function that appends string to a text file"""


def append_file(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
