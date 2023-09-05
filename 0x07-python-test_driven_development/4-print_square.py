def print_square(size):
    """
    Prints a square with the character '#' of the given size.

    Args:
        size (int): The size (length) of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0 or a non-integer float.

    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0 or (isinstance(size, float) and not size.is_integer()):
        raise ValueError("size must be a non-negative integer")

    for i in range(size):
        print("#" * size)
