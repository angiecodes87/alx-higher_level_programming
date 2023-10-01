#!/usr/bin/python3
"""
This module contains a function that divides the numbers of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides the integer/float numbers of a matrix by a given number.

    Args:
        matrix (list of lists): A list of lists containing integers/floats.
        div (int or float): The number by which to divide the matrix.

    Returns:
        list of lists: A new matrix with the result of the division.

    Raises:
        TypeError: If the elements of the matrix aren't lists,
            If the elements of the lists aren't integers/floats,
            If div is not an integer/float number,
            If the lists of the matrix don't have the same size.
            ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_type_error_msg = "matrix must be a matrix(list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_type_error_msg)
    len_e = 0
    size_error_msg = "Each row of the matrix must have the same size"

    for elems in matrix:
        if not elems or not isinstance(elems, list):
            raise TypeError(matrix_type_error_msg)

        if len_e != 0 and len(elems) != len_e:
            raise TypeError(size_error_msg)

    for num in elems:
        if not isinstance(num, (int, float)):
            raise TypeError(matrix_type_error_msg)

    len_e = len(elems)

    result_matrix = [
        [round(num / div, 2) for num in elems]
        for elems in matrix
    ]

    return result_matrix
