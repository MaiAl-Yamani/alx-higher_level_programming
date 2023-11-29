#!/usr/bin/python3
"""This is locked_class module"""


class LockedClass:
    """
    A class that prevents user from instatiating new attributes
    other than first_name attribute.
    """
    __slots__ = ["first_name"]
