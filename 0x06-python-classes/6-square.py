#!/usr/bin/python3
"""
This is a Square module

This module defines a simple square by an integer size instance attribute
Default size is 0, and raises errors on invalid input
Methods getter and setter for size attribute
Method area returns area of the square.
Method my_print that prints in stdout the square with "#"
"""


class Square:
    """A class that defines a square by size and computes Area"""
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
        if self.__position[0] >= 0 and self.__position[1] >= 0:
            self.__position = position
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

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
