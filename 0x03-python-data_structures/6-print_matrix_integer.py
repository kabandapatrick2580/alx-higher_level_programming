#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_num in row:
            print("{:d}".format(col_num), end =" ")
        print()
