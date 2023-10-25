#!/usr/bin/python3
"""
Defines lazy_matrix function
"""
import numpy as np

def lazy_matrix_multiply(matrix_a, matrix_b):
    """Calculates the matrix multiplication of two matrices"""
    return np.matmul(matrix_a, matrix_b)
