#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args_list):
    filename = "add_item.json"

    if exists(filename):
        my_list = load_from_json_file(filename
    else:
        my_list = []

    my_list.extend(args_list)
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    args = sys.argv[1:]
    add_item(args)
