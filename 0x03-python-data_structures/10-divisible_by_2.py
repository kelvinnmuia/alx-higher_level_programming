#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mps = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mps.append(True)
        else:
            mps.append(False)

    return (mps)
