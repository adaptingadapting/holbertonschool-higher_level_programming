#!/usr/bin/python3

""" module for caluclating the multiplication of matrices
using the numpy module """


import numpy


def lazy_matrix_mul(m_a, m_b):
    """ i thought we had to do the checks, oops """
    return numpy.matmul(m_a, m_b)
