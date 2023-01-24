#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    my_new_matrix = []
    for i in range(len(matrix)):
        my_new_matrix.append([])
        for j in range(len(matrix[i])):
            my_new_matrix[i].append(matrix[i][j]**2)
    return my_new_matrix
