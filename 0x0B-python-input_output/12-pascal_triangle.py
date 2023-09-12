#!/usr/bin/python3
"""Module for generating Pascal's triangle."""


def pascal_triangle(n):
    """
    Create Pascal's triangle up to a specified number of rows.

    Args:
        n (int): An integer indicating the nb of rows in the Pascal's triangle.

    Returns:
        list: A list of lists contain intgrs representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        current_row = [1]
        previous_row = triangle[i - 1]
        for j in range(1, i):
            current_row.append(previous_row[j - 1] + previous_row[j])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
