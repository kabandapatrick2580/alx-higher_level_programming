#!/usr/bin/python3
"""Defining a class"""


class Square:
    """Square Class Representation"""
    def __init__(self, size=0):
        """
        Initialisation of a Square

        If size is not an integer, Raise an exception error
        of TypeError with a message attached.

        Make sure the size is greater than zero, otherwise raise
        an exception error of ValueError with a messaga attached.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """
        This setting of self.__size is done after checking
        the size and value tests.
        """
