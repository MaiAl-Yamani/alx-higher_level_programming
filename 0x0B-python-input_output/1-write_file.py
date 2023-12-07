#!/usr/bin/python3
"""This is 1-write_file module."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of chars written"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
