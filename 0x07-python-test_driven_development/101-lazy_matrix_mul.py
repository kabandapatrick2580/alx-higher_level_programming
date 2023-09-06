import NumPy as np
""" Multiplying two matrices using numpy module"""

def lazy_matrix_mul(m_a, m_b):
    """
    Args:
        m_a (list): Matrix A represented as a list of lists of integers.
        m_b (list): Matrix B represented as a list of lists of integers.

    Returns:
        list: Result of the multiplication of two matrices as a NumPy array.

    Raises:
        ValueError: setting an array element with a sequence.
    """
    res = np.matmul(m_a, m_b)
    return res

