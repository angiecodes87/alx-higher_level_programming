#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number of
    characters added.

    Args:
        filename (str): The name of the file to append. (default: "")
        text (str): The text to be appended. (default: "")

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
