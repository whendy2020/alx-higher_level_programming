#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = sum(list(map(lambda a: a, set(my_list))))
    return result
