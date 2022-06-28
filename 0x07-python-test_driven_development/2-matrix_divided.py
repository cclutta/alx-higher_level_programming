#!/usr/bin/python3
"""
matrix_divided module

Has one function matrix_divided()
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix where each element has been divided by div.
    Args:
        matrix (list): list of lists of integers or floats.
        div (int, float): the divider, >= 0.
    """
    mtrx_type_e = 'matrix must be a matrix (list of lists) of integers/floats'
    mtrx_len_e = 'Each row of the matrix must have the same size'
    div_type_e = 'div must be a number'
    div_zero_e = 'division by zero'

    row_len = 0
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix \
            (list of lists) of integers/floats')

    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix \
                (list of lists) of integers/floats')
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError('matrix must be a matrix \
                    (list of lists) of integers/floats')
        if len(row) is not row_len and row_len is not 0:
            raise TypeError('Each row of the matrix must \
                have the same size')
        row_len = len(row)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    return [[round(nb / div, 2) for nb in row] for row in matrix]
