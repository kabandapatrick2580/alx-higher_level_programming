#!/usr/bin/python3
"""Geometry module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, based on BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If the width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string describing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
