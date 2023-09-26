#!/usr/bin/python3
"""exception and stderr for a function that executes a function safely.

arguments:
    fct: the function
    args: the fct arguments

Return: returns a function call
"""


import sys

def safe_function(fct, *args):
    try:
        reslt = fct(*args)
        return reslt
    except Exception as e:
        print("Exception: {}".format(str(e), file=sys.stderr)
        return None
