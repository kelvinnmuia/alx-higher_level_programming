#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
        except Exception as e:
            pass
        else:
            output += (a ** b) / i
    return output