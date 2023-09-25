#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
    try:
        count = 0
        for element in my_list:
            if count < x:
                print(element, end=" ")
                count += 1
            else:
                break
            print()
            return count
        except TypeError:
            print("Error: my_list is not a valid error.")
            return 0
