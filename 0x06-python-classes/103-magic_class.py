#!/usr/bin/python3
"""Magic class"""


import math


class MagicClass:
    """A class that defines area and circumference using radius"""
    def __init__(self, radius=0):
        """Initialization method"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Returns the area of MagicClass"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Return the circumference of MagicClass"""
        return 2 * math.pi * self.__radius
