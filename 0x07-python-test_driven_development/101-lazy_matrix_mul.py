def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using the NumPy module.

    Args:
        m_a (list): Matrix A represented as a list of lists of integers.
        m_b (list): Matrix B represented as a list of lists of integers.

    Returns:
        list: Result of the multiplication of two matrices as a NumPy array.

    Raises:
        ValueError: If m_a and m_b cannot be multiplied.
    """

    res = np.matmul(m_a, m_b)
    return res

