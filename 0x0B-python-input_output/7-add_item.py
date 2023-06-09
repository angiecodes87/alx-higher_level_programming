#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys
from os.path import exists
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file

filename = "add_item.json"

if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)
