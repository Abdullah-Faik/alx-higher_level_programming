#!/usr/bin/python3
""" This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ This function divides all elements of a matrix
    Args:
        matrix (list): list of lists of integers or floats
        div (int/float): number to divide matrix by
    Returns:
        list: list of lists of quotients
    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if matrix rows are not the same size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is 0
    """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix \
                                 (list of lists) of integers/floats")
    return [[round(num / div, 2) for num in row] for row in matrix]
