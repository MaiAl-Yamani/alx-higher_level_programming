#!/usr/bin/python3
"""This is rectangle.py module."""
from models.base import Base


class Rectangle(Base):
    """This is Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation method."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter."""
        self.__width = width

    @property
    def height(self):
        """height getter."""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """x attribute getter."""
        return self.__x

    @x.setter
    def x(self, x):
        """x attribute setter."""
        self.__x = x

    @property
    def y(self):
        """y attribute getter."""
        return self.__y

    @y.setter
    def y(self, y):
        """y attribute setter."""
        self.__y = y
