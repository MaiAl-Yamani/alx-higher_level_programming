#!/usr/bin/python3
# 1-rectangle.py
# Mai Elyamani <mai.elyamni@gmail.com>
"""This is 1-rectangle module."""


class Rectangle:
    """A Recyangle class defined by its width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.__height = height
        self.__width = width

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
