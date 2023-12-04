#!/usr/bin/python3
"""This is 3-is_kind_of_class module."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of the class or class that inherits from it.

    Args:
        obj (any): object to check.
        a_class: class to match.
    Returns:
        True - if obj is an instance of a class or class the inherits from it.
        False - otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
