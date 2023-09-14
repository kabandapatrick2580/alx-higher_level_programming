#!/usr/bin/python3
"""Geometry module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square, based on the Rectangle class."""

    def __init__(self, size):
        """
        Initialize a Square object with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string describing the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
