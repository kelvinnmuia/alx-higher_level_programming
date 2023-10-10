#!/usr/bin/python3
""" defines a function that reads text file and prints to stdout"""


def read_file(filename=""):
    """ reads text file and prints to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
