#!/usr/bin/python3
"""class Definition"""


class Square:
    """Square class representation"""
    def __init__(self, size=0):
        """
        Initialisation a Square

        If size is not an integer, raise an exception error
        of TypeError with a message attached.

        Make sure the size is greater than or equal to zero,
        otherwise raise an exception error of ValueError
        with a message attached.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance method that returns
        the current area of a square.
        """
        return self.__size * self.__size
