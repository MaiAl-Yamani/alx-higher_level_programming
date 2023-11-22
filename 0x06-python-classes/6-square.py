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
        """initialization method"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """size setter"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """returns square area"""
        return self.__size * self.__size

    def my_print(self):
        """prints to stdout square using #"""
        if self.__size == 0:
            print()
            return
        else:
            for j in range(0, self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
