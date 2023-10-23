#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    for i in range(0, x):
        try:
            x = my_list[i]
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
    print()
    return i
