#!/usr/bin/python3
"""Defines a class named Rectangle."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    number_of_instances = 0  # Class attribute to keep track of instances

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1  # Increment class attribute

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle as '#' symbols."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    def __repr__(self):
        """
        Return a string representation of the Rectangle.

        This can be used to recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance is deleted.

        Also, decrement the class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement class attribute
