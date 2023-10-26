#!/usr/bin/python3
"""find the area of a square"""


class Square:
    """ private instance attribute size must be int"""
    def __init__(self, size=0):
        """private instance attribute size"""
        self.__size = size
        size: int

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """a public instance class to calc the area of a circle"""
        return self.__size ** 2
