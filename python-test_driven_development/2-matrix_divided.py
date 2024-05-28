#!/usr/bin/python3
"""

This module is composed by a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    matrix (list of lists): A matrix to be divided, must be a list of lists
    of integers or floats.
    div (int or float): The divisor, must be a non-zero number

    Returns:
    list of lists: A new matrix with all elements divided by the divisor,
    rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats,
    or if div is not a number.
    TypeError: If each row of the matrix does not have the same size.
    ZeroDivisionError: If div is equal to 0.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
