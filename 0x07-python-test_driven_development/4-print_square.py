#!/usr/bin/python3
"""This is 4-print_square module: prints a square of a specific size."""


def print_square(size):
    """Prints a square by its size using #."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
