#!/usr/bin/python3
"""
Contains the matrix_multiply function
"""


def matrix_multiply(matrix_a, matrix_b):
    """Multiply two matrices (lists of lists of integers/floats)"""
    if type(matrix_a) is not list:
        raise TypeError("matrix_a must be a list")
    rows_a = len(matrix_a)
    if rows_a == 0:
        raise ValueError("matrix_a can't be empty")
    cols_a = None
    for row in matrix_a:
        if type(row) is not list:
            raise TypeError("matrix_a must be a list of lists")
        if cols_a is None:
            cols_a = len(row)
            if cols_a == 0:
                raise ValueError("matrix_a can't be empty")
        if cols_a != len(row):
            raise TypeError("each row of matrix_a must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix_a should contain only integers or floats")

    if type(matrix_b) is not list:
        raise TypeError("matrix_b must be a list")
    if len(matrix_b) == 0:
        raise ValueError("matrix_b can't be empty")
    cols_b = None
    for row in matrix_b:
        if type(row) is not list:
            raise TypeError("matrix_b must be a list of lists")
        if cols_b is None:
            cols_b = len(row)
            if cols_b == 0:
                raise ValueError("matrix_b can't be empty")
        if cols_b != len(row):
            raise TypeError("each row of matrix_b must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix_b should contain only integers or floats")

    if cols_a != len(matrix_b):
        raise ValueError("matrix_a and matrix_b can't be multiplied")

    result_matrix = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            value = 0
            for k in range(cols_a):
                value += matrix_a[i][k] * matrix_b[k][j]
            row.append(value)
        result_matrix.append(row)

    return result_matrix
