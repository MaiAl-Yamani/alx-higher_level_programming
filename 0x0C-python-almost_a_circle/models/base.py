#!/usr/bin/python3
"""This is base.py module."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
