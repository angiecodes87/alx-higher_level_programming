#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    A base geometry class.

        This class serves as the base class for other geometry classes.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.

        """
        raise Exception("area() is not implemented")
