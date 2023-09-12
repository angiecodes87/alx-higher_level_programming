#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters
    written.

    Args:
        filename (str): The name of the file to write. (default: "")
        text (str): The text to be written. (default: "")

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters = file.write(text)
    return num_characters
