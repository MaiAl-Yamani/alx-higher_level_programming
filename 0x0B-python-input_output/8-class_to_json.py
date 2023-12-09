#!/usr/bin/python3
"""This is 8-class_to_json module."""
import json


def class_to_json(obj):
    """Returns the dictionary description with simple data structure."""
    return obj.__dict__
