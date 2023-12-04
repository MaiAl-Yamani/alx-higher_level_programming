#!/usr/bin/python3
"""This is 2-is_same_class module."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check if it is exactly an instance.
        a_class (type): the class to match the type of obj to.
    Returns:
        True if the type of obj is exactly an instance of a_class.
        False therwise.
    """
    if type(obj) == a_class:
        return True
    return False
