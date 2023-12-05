#!/usr/bin/python3
"""This is 101-lazy_matrix_mul module."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices using numpy."""
    return np.dot(m_a, m_b)
