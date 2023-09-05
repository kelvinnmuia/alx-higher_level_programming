#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 'a' <= ch <= 'z':
            uppercase_ch = chr(ord(ch) - 32)
        else:
            uppercase_ch = ch
            print(uppercase_ch, end='')


print()
