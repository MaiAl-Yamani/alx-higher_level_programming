#!/usr/bin/python3
"""This is base.py module."""


class Base:
    """This is Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
