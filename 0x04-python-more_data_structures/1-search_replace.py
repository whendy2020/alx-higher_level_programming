#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = list(map(lambda x: replace if x in new_list and search == x else x, new_list))
    return new_list
