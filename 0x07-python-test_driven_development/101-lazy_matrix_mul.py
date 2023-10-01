#!/usr/bin/python3
"""
Defines a function for matrix multiplication using NumPy.
"""

import numpy as np

def matrix_multiplication(m_a, m_b):
    """
    Multiply two matrices using NumPy arrays.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    if not isinstance(m_a, np.ndarray) or not isinstance(m_b, np.ndarray):
        raise TypeError("m_a and m_b must be NumPy arrays")

    result_matrix = np.matmul(m_a, m_b)
    return result_matrix
