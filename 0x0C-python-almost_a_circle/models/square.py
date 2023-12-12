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
        return self.width

    @size.setter
    def size(self, size):
        """size attribute setter."""
        self.integer_validator("width", size)
        self.width = size
        self.height = size

    def __str__(self):
        """Returns print/str representation."""
        string = "[" + str(type(self).__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.size)
        return string

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if not args or args is None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            if i == 1:
                self.size = args[i]
            if i == 2:
                self.x = args[i]
            if i == 3:
                self.y = args[i]

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
