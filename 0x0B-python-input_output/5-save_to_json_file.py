#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to save the JSON representation.

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
