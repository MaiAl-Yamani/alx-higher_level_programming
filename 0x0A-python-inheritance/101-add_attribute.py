#!/usr/bin/python3
"""This is 101-add_attribute module."""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it’s possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
