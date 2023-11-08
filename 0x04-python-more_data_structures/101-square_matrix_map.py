#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
#    return [[x for x in map((lambda x: x ** 2), matrix[r])] for r in range(len(matrix))]
