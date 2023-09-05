#!/usr/bin/python3
"""
This module contains a function that adds two numbers.
"""


def add_integer(a, b=98):
    """Adds two integer or float numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of the two given numbers as an integer.

    Raises:
        TypeError: If a or b are not integer or float numbers.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be integer or float numbers")

    return int(a) + int(b)
