#!/usr/bin/python3
"""
Module composed of a function that adds two new lines after ".?:" characters.
"""

def text_indentation(text):
    """Prints 2 new lines after ".?:" characters in the input string.

    Args:
        text (str): The input string.

    Returns:
        None

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = text
    for char in ".?:":  # Iterate over ".", "?", and ":"
        result = result.replace(char, f"{char}\n\n")

    print(result, end="")
