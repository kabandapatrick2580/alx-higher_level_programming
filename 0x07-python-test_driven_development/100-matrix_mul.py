def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list): Matrix A represented as a list of lists of integers or floats.
        m_b (list): Matrix B represented as a list of lists of integers or floats.

    Returns:
        list: Result of the multiplication of two matrices.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        ValueError: If m_a or m_b is empty or contains empty lists.
        TypeError: If m_a or m_b contains elements that are not integers or floats.
        TypeError: If rows of m_a and m_b do not have the same size.
        ValueError: If the number of columns in m_a is not equal to the number of rows in m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or any(not row for row in m_a):
        raise ValueError("m_a can't be empty or contain empty lists")
    if m_b == [] or any(not row for row in m_b):
        raise ValueError("m_b can't be empty or contain empty lists")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m1 = []
    for i in range(len(m_b[0])):
        my_row = []
        for j in range(len(m_b)):
            my_row.append(m_b[j][i])
        m1.append(my_row)

    m2 = []
    for row in m_a:
        my_row = []
        for column in m1:
            product = 0
            for m in range(len(m1[0])):
                product += row[m] * column[m]
            my_row.append(product)
        m2.append(my_row)

    return m2
