#!/usr/bin/python3

def replace_in_list(my_list, idx, new_element):
    if my_list:
        leng = len(my_list) - 1
        if idx < 0:
            return my_list
        if idx > leng:
            return my_list
        my_list[idx] = new_element
        new_list = my_list
        return my_list
