#!/usr/bin/python3
"""
This is a Square module

This module defines a simple square by an integer size instance attribute
Default size is 0, and raises errors on invalid input
Position attribute default (0, 0) tuple
Methods getter and setter for size and position attributes
Method area returns area of the square
Method my_print that prints the square with "#" moving from left and top
using position tuple
"""


class Square:
    """
    A class that defines a square by size (default 0)
    And position tuple (default (0, 0))
    Can compute area and print the square using "#"
    There is a position offset on left and top of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
                not all([type(i) == int for i in value]) or \
                not all([i >= 0 for i in value]):
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
