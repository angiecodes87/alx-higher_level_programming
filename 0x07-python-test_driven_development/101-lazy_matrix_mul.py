#!/usr/bin/python3
"""
This script defines a function for lazy matrix multiplication using NumPy.
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices represented as NumPy arrays.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    Raises:
        ValueError: If the input matrices are incompatible for multiplication.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")
    
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)

    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("Matrix dimensions are not compatible for multiplication")
    
    result_matrix = np.matmul(matrix_a, matrix_b)
    return result_matrix
