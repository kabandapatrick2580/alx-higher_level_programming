def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list): A list of lists representing the matrix.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a valid matrix of integers or floats.
        TypeError: If all rows in the matrix do not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to zero, preventing division by zero.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elem, int) or isinstance(elem, float))
                    for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    div_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return div_matrix
