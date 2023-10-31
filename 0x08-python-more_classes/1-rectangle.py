#!/usr/bin/python3
"""Define width and height"""


class Rectangle:
    """Class Rectangle attributes"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        width: int
        height: int
        
            
        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, value):
            if not type(height):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        
        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            if not type(width):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
