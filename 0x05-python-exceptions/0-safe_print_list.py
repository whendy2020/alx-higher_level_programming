#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    for i in range(0, x):
        try:
            x = my_list[i]
            print(my_list[i], end="")
        except IndexError:
            break
    print()
    return x
