#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_num in range (len(row)):
            if col_num != len(row) -1:
                print("{:d}".format(row[col_num]), end =" ")
            else:
                print("{:d}".format(row[col_num], end = ""))
        print()
