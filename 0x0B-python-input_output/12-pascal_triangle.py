#!/usr/bin/python3
"""
Module 12-pascal_triangle
Returns a list of lists of integers rep Pascal's triagle of n

"""


def pascal_triangle(n):
    """ Return Pascal triagle of n) """
    if n < 0:
        return []
    tri = [[0 for j in range(i + 1)] for i in range(n)]
    tri[0] = [1]
    for i in range(1, n):
        tri[i][0] = 1
        for j in range(1, i + 1):
            if j < len(tri[i - 1]):
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]
            else:
                tri[i][j] = tri[i - 1][0]
    return tri
