#!/usr/bin/python3
"""This is 100-my_int module: defines MyInt class that inherets from int."""


class MyInt(int):
    """MyInt class: inverts == and != behaviors."""

    def __eq__(self, value):
        """override == operator to != operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != operatr to == operator."""
        return self.real == value
