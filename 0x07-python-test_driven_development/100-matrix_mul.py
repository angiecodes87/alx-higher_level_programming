#!/usr/bin/python3
"""
This script defines a matrix multiplication function.
"""

def matrix_multiply(matrix_a, matrix_b):
    """
    Multiply two matrices represented as lists of lists of integers/floats.
    
    Args:
        matrix_a (list): The first matrix.
        matrix_b (list): The second matrix.
    
    Returns:
        list: The result of the matrix multiplication.
    
    Raises:
        TypeError: If the input matrices are not of the expected type.
        ValueError: If the input matrices are empty or incompatible for multiplication.
    """
    if type(matrix_a) is not list:
        raise TypeError("matrix_a must be a list")
    
    num_rows_a = len(matrix_a)
    if num_rows_a == 0:
        raise ValueError("matrix_a can't be empty")
    
    num_cols_a = None
    for row in matrix_a:
        if type(row) is not list:
            raise TypeError("matrix_a must be a list of lists")
        
        if num_cols_a is None:
            num_cols_a = len(row)
            if num_cols_a == 0:
                raise ValueError("matrix_a can't be empty")
        
        if num_cols_a != len(row):
            raise TypeError("each row of matrix_a must have the same size")
        
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix_a should contain only integers or floats")

    if type(matrix_b) is not list:
        raise TypeError("matrix_b must be a list")
    
    num_rows_b = len(matrix_b)
    if num_rows_b == 0:
        raise ValueError("matrix_b can't be empty")
    
    num_cols_b = None
    for row in matrix_b:
        if type(row) is not list:
            raise TypeError("matrix_b must be a list of lists")
        
        if num_cols_b is None:
            num_cols_b = len(row)
            if num_cols_b == 0:
                raise ValueError("matrix_b can't be empty")
        
        if num_cols_b != len(row):
            raise TypeError("each row of matrix_b must have the same size")
        
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix_b should contain only integers or floats")

    if num_cols_a != num_rows_b:
        raise ValueError("matrix_a and matrix_b can't be multiplied")
    
    result_matrix = []
    
    for i in range(num_rows_a):
        row_result = []
        for j in range(num_cols_b):
            element_sum = 0
            for k in range(num_cols_a):
                element_sum += matrix_a[i][k] * matrix_b[k][j]
            row_result.append(element_sum)
        result_matrix.append(row_result)
    
    return result_matrix
