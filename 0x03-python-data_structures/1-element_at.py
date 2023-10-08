#!/usr/bin/python3

def element_at(my_list, idx):
    leng = len(my_list) - 1
    if idx < 0:
        return None
    if idx > leng:
        return None
    for i in range(0, leng):
        my_list[idx]
    return my_list[idx]
