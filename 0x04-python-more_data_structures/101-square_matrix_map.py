#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [[x for x in map((lambda x: x ** 2), matrix[r])] for r in range(len(matrix))]
