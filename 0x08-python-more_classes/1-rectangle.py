#!/usr/bin/python3
"""Defines a class named Rectangle."""


class Rectangle:
    """This class represents a Rectangle shape."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with specified
        width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle with error handling."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle with error handling."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
