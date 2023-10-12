#!/usr/bin/python3
"""
This is the "matrix divided" module.

The matrix divided module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix with all the elements divided by div.
    """
    errorMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(errorMsg)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(errorMsg)
        for column in matrix[0]:
            if type(column) is not int and type(column) is not float:
                raise TypeError(errorMsg)

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new = [row[:] for row in matrix]
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            new[row][column] = round(matrix[row][column] / div, 2)

    return new
