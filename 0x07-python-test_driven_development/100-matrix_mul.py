#!/usr/bin/python3
"""defines a function that multiplies two matrices and
returns a new matrix containing the product"""


def matrix_mul(m_a, m_b):
    """multiplies two matrices and returns products in new matrix"""

    # checking whether the matrices are list of lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # validating that the matrices are list of lists
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    # ensuring the matrices aren't empty
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    # validating that matrices have the correct type
    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or float")

    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or float")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # check whether the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # initializing the resulting matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Nested loops to compute the product of the matrices elements
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
