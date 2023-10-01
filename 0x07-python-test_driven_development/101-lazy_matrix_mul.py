#!/usr/bin/python3
"""
Defines a function for matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
     """
    Multiply two matrices represented as NumPy arrays.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.
    """
    return numpy.matmul(m_a, m_b)
