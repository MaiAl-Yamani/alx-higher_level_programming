#!/usr/bin/python3
"""This is models/square.py module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation method."""
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size attribute getter."""
        return self.__size

    @size.setter
    def size(self, size):
        """size attribute setter."""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns print/str representation."""
        string = "[" + str(type(self).__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.size)
        return string
