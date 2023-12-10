#!/usr/bin/python3
"""This is rectangle.py module."""
from models.base import Base


class Rectangle(Base):
    """This is Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation method."""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
        self.integer_validator("x", x)
        self.x = x
        self.integer_validator("y", y)
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter."""
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """height getter."""
        return self.__height

    @height.setter
    def height(self, height):
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """x attribute getter."""
        return self.__x

    @x.setter
    def x(self, x):
        """x attribute setter."""
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """y attribute getter."""
        return self.__y

    @y.setter
    def y(self, y):
        """y attribute setter."""
        self.integer_validator("y", y)
        self.__y = y

    def integer_validator(self, name, value):
        """Method that validates value.

        Args:
            name (str): name of attribute.
            value (int): value of the attribute.
        Raises:
            TypeError: if value is not int.
            ValueError: if value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns area of a rectangle."""
        return self.width * self.height
