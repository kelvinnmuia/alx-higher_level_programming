#!/usr/bin/python3
def uppercase(str):
    output = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
            output += ch
        print("{}".format(output), end="")
