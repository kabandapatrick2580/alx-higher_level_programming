#!/usr/bin/python3
"""Module for geometry-related operations."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Calculate the area of the geometric shape.

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")
