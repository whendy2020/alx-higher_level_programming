#!/usr/bin/python3

def max_integer(my_list=[]):
    leng = len(my_list) - 1
    if not my_list:
        return None
    else:
        max_value = my_list[0]
        for i in range(0, leng):
            if my_list[i] > max_value:
                max_value = my_list[i]
                return max_value
