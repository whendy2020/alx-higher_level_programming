#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    od_set = set_2.symmetric_difference(set_1)
    return od_set
