#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            squared_element = matrix[i][j] ** 2
            row.append(squared_element)
        squared_matrix.append(row)
    return squared_matrix
