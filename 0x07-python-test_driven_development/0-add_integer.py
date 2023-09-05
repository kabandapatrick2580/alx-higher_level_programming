#!/usr/bin/python3
"""This module is for adding two integers or floats as integers."""


def add_integer(a, b=98):
    """Returns the sum of two integers or floats as integers.

    Args:
        a (int or float): The first argument.
        b (int or float, optional): The second argument. Defaults to 98.

    Returns:
        int: The sum of the arguments.

    Raises:
        TypeError: If either of the arguments is not an integer or a float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")

    a = int(a)
    b = int(b)

    return a + b
