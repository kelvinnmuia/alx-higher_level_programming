#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda n: n * n, r)) for r in matrix])
