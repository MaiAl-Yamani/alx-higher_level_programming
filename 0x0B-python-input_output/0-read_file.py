#!/usr/bin/python3
"""This is 0-read_file module."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end='')
