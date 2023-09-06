#!/usr/bin/python3
def pow(a, b):
    output = 1

    if b >= 0:
        for _ in range(b):
            output *= a
    else:
        for _ in range(-b):
            output /= a
    return output 
