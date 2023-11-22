#!/usr/bin/python3
"""
This is a Square module

This module defines a simple square by an integer size instance attribute
Default size is 0, and raises errors on invalid input
Methods getter and setter for size attribute
Method area returns area of the square.
"""


class Square:
    """A class that defines a square by size and computes Area"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int) or not isinstance(size, float):
            raise TypeError('size must be a number')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size**2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
