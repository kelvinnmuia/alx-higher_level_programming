#!/usr/bin/python3
"""Defines function for multiplying two matrices using Numpy"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns their products
    
    Args:
        m_a (list[list[int or float]]): The first matrix
        m_b (list[list[int or float]]): The second matrix
    """
    return (np.matmul(m_a, m_b))
