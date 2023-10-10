#!/usr/bin/bash

def add_tuple(tuple_a=(), tuple_b=()):
    zero_tup = (0, 0)
    if len(tuple_a) < 2:
        tuple_a + zero_tup

    if len(tuple_b) < 2:
        tuple_b + zero_tup
    if tuple_a > 2:
        new_tuple = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return new_tuple
