#!/usr/bin/python3

def max_integer(my_list=[]):
    max_value = my_list[0]
    leng = len(my_list) - 1
    if len(my_list) == 0:
        return None
    else:
        for i in range(0, leng):
            if my_list[i] > max_value:
                max_value = my_list[i]
                return max_value
