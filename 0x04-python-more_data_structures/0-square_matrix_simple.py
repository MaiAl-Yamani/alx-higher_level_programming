#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(len(matrix)):
        row_list = []
        for col in range(len(matrix[0])):
            row_list.append(matrix[row][col] ** 2)
        new_matrix.append(row_list)
    return new_matrix
