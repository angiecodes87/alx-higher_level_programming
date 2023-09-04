#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.
        Args:
            Width(int): The width of a new rectangle.
            height(int): The height of the new rectangle.
        """
    self.__width = width
    self.__height = height

    @property
    """Get width of the rectangle. """
    def width(self):
        return self.__width

    @width.setter
     """ Get and set width for the rectangle" """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
    self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
     self.__height = value

