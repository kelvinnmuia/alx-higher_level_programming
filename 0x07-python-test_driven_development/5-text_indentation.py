#!/usr/bin/python3
"""defines a function to print text with 2 newlines after '?''.' ':'"""


def text_indentation(text):
    """prints text with 2 newlinnes after '?' '.' ':'"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    beg = ""
    for ch in text:
        #checking leading whitespaces
        if ch == " " and ch in text[0] and beg == "":
            beg = "\n"
            continue
        #checking  trailling whitespaces
        if ch == " " and beg == "\n":
            continue
        #match the characters
        if ch == "." or ch == "?" or ch == ":":
            print(ch)
            print()
            beg = "\n"
        else:
            print(ch, end="")
            beg = ch
