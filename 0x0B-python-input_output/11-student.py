#!/usr/bin/python3
"""This is 10-student module."""


class Student:
    """This is Student class."""

    def __init__(self, first_name, last_name, age):
        """Instantiation method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        new = dict()
        if type(attrs) is list and all(type(key) is str for key in attrs):
            for key in attrs:
                if key in self.__dict__:
                    new[key] = self.__dict__[key]
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        if not json:
            return
        self.__dict__ = json
