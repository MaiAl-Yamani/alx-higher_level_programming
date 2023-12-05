#!/usr/bin/python3
"""This is 7-base_geometry module."""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """Method that is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value.

        Args:
            name (str): name of the parameter.
            value (int): value of the parameter.
        Raises:
            TypeError: if value is not int.
            ValueError: if value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
