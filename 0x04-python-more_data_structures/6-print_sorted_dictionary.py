#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
    return a_dictionary
