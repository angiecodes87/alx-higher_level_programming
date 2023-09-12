#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description of the object.

    """
    return obj.__dict__
