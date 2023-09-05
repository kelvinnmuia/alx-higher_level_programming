#!/usr/bin/python3
for fd in range(10):
    for sd in range(fd + 1, 10):
        if fd == 8 and sd == 9:
            print("{:02d}".format(fd * 10 + sd))
        else:
            print("{:02d}, ".format(fd * 10 + sd), end="")
