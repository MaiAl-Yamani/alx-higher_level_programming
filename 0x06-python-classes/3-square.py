#!/usr/bin/python3
"""
This is a Square module

This module defines a simple square by an integer size instance attribute
Default size is 0, and raises errors on invalid input
Method area returns area of the square.
"""


class Square:
    """A class that defines a square by size and can get area of the square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
