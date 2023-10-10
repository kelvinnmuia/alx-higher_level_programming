#!/usr/bin/python3
""" defines function that writes string to a text file"""


def write_file(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'w') as f:
        return f.write(text)
