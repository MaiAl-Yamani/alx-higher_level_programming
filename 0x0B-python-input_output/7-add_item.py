#!/usr/bin/python3
"""This is 7-add_item module."""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except Exception as e:
    content = []

for i in range(1, len(argv)):
    content.append(argv[i])
save_to_json_file(content, filename)
