#!/usr/bin/python3
"""This is 4-inherits_from module."""


def inherits_from(obj, a_class):
    """Check if obj is an inherited instance of a specified class.

    Args:
        obj (any): object to check.
        a_class (type): class to match.
    Returns:
        True - if obj is inherited instance from a_class.
        False - otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
