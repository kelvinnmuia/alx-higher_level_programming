#!/usr/bin/python3
"""defines a function to divide matrix with single value"""


def matrix_divided(matrix, div):
    """divides the matrix with single value"""
    import decimal
    err_mesg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_mesg)
    rows_ln = []
    row_counter = 0

    for row in matrix:
        if type(row) is not list:
            raise TypeError(err_mesg)
        rows_ln.append(len(row))
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(err_mesg)
        row_counter += 1
    if len(set(rows_ln)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(div) == 0:
        raise ZeroDivisionError("division by zero")
    rs_matrix = list(map(lambda row:
                         list(map(lambda r: round(r/div, 2), row)), matrix))
    return rs_matrix
