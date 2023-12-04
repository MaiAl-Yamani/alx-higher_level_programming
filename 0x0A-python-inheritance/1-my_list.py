#!/usr/bin/python3
"""This is my_list module."""


class MyList(list):
    """A sub-class that inherits from list class"""
    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
