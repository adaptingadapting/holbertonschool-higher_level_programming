#!/usr/bin/python3

""" module for multiplying matries """


def matrix_mul(m_a, m_b):
    """ matrix mul lots of excpetions at the start
    the matrix multiplication is at the botttom """

    if not type(m_a) == list:
        raise TypeError("m_a must be a list")
    if not type(m_b) == list:
        raise TypeError("m_b must be a list")
    if not all(type(row) == list for row in m_a) or m_a == []:
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) == list for row in m_b) or m_b == []:
        raise TypeError("m_b must be a list of lists")
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(type(num) in [int, float] for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(num) in [int, float] for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    orig_len_a = len(m_a[0])
    orig_len_b = len(m_b[0])

    if not all(len(row) == orig_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == orig_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    result = 0
    new_matrix = []
    new_row = []

    for i in range(len(m_a)):
        for k in range(len(m_a)):
            for j in range(len(m_a[i])):
                if len(m_a[i]) > len(m_b[0]):
                    raise ValueError("m_a and m_b can't be multiplied")
                result += m_a[i][j] * m_b[j][k]
            new_row.append(result)
            result = 0
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
