#!/usr/bin/python3

def pascal_triangle(n):
    """ pascal triangle """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        vir = triangles[-1]
        tmp = [1]
        for i in range(len(vir) - 1):
            tmp.append(vir[i] + vir[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
