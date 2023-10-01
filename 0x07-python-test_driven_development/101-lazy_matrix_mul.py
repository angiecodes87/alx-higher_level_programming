#!/usr/bin/python3
"""
This script defines a function for lazy matrix multiplication using NumPy.
"""

import numpy as np

def lazy_matrix_multiply(matrix_a, matrix_b):
    """
    Perform matrix multiplication of two matrices using NumPy.

    Args:
        matrix_a (numpy.ndarray): The first matrix.
        matrix_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    Raises:
        ValueError: If the input matrices are incompatible for multiplication.
    """
    if not isinstance(matrix_a, np.ndarray) or not isinstance(matrix_b, np.ndarray):
        raise TypeError("Both input matrices must be NumPy arrays")
    
    if matrix_a.shape[1] != matrix_b.shape[0]:
        raise ValueError("Matrix dimensions are not compatible for multiplication")
    
    result_matrix = np.matmul(matrix_a, matrix_b)
    return result_matrix
