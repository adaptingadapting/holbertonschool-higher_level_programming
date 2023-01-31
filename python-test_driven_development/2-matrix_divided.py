#!/usr/bin/python3

""" Module for dividing a matrix """


def matrix_divided(matrix, div):
    """ divides a matrix between div, various errors are detected """

    if (not matrix or matrix == [] or not all(type(row) == list for row
        in matrix) or not all(type(num) in [float, int] for row in
                              matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of\
 integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not type(div) in [float, int]:
        raise TypeError("div must be a number")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
