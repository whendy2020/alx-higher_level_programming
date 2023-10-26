#!/usr/bin/python3
"""Instantiation with optional size: def __init__(self, size=0):"""


class Square:
    """ private instance attribute size must be int"""
    def __init__(self, size=0):
        self.__size = size
        size: int

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
