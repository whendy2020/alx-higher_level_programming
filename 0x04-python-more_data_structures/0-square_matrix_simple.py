#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    leng = len(matrix)
    new_matrix = matrix.copy()
    for i in range(leng):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return new_matrix
