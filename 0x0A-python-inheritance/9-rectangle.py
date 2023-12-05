#!/usr/bin/python3
"""This is 8-rectangle module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class."""

    def __init__(self, width, height):
        """Instantiation method for a new rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns print/string representation of a rectangle."""
        string = "[" + str(type(self).__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
