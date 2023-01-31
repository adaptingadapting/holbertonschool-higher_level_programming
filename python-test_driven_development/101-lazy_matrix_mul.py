#!/usr/bin/python3

""" module for caluclating the multiplication of matrices
using the numpy module """


import numpy


def lazy_matrix_mul(m_a, m_b):
    """ using numpy is easier, i made some improvements too """
    if type(m_a) is not list:
        raise TypeError("m_a is not list")
    if type(m_b) is not list:
        raise TypeError("m_b is not list")
    if not all(type(row) is list for row in m_a) or m_a == []:
        raise TypeError("m_a is not a list of lists")
    if not all(type(row) is list for row in m_b) or m_b == []:
        raise TypeError("m_b is not a list of lists")
    if m_a == [[]]:
        raise ValueError("m_a cant be empty")
    if m_b == [[]]:
        raise ValueError("m_b cant be empty")
    if not all(type(num) in [int, float] for row in m_a for num in row):
        raise TypeError("m_a has to contain only integers or floats")
    if not all(type(num) in [int, float] for row in m_b for num in row):
        raise TypeError("m_b has to contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be equal in size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be equal in size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cant multiply")
    return numpy.matmul(m_a, m_b)
