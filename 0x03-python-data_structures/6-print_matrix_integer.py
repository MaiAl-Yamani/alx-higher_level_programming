#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_count = len(matrix)
    col_count = len(matrix[0])
    for row in range(row_count):
        for col in range(col_count):
            if col == col_count - 1:
                print("{:d}".format(matrix[row][col]), end='')
            else:
                print("{:d} ".format(matrix[row][col]), end='')
        print("")
