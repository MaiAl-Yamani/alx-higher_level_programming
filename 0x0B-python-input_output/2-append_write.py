#!/usr/bin/python3
"""This is 2-append_write module."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file."""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
