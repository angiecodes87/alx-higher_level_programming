#!/usr/bin/python3
"""
This script defines a matrix multiplication function.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices represented as lists of lists of integers or floats.
    
    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, contains non-integer or non-float elements, or has rows of different sizes.
        ValueError: If m_a or m_b is empty or if they can't be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")
    
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return result_matrix

