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

matrix = [[1,2,3],[3,4,5],[6,7,8,9]]
square = square_matrix_simple(matrix)
print(square)
print(matrix)
