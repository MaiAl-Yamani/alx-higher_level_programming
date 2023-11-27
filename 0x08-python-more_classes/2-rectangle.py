#!/usr/bin/python3
"""
This is a "Rectangle" module.

This module defines a simple rectangle by an integer width and height
Default width and height are 0, and raises errors on invalid input
Methods getter and setter for width and height attributes
Method area that returns area of the rectangle
Method perimeter that returns perimeter of the rectangle.
"""


class Rectangle:
    """A Recyangle class defined by its width and height."""
    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)
