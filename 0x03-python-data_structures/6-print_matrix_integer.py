#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_num in row:
            if col_num == row[-1]:
                print("{:d}".format(col_num), end ="")
            else:
                print("{:d}".format(col_num), end = " ")
        print()
