#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not j:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print(" ", end="")
                print("{:d}".format(matrix[i][j]), end="")
        print()
