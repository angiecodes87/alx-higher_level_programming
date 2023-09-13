#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly
    or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of a class that inherited (directly
        or indirectly) from the specified class; otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
