#!/usr/bin/python3

"""Defining a class"""


class Square:
    """
    Representation of a Square.

    Attributes:
    - size: The size of the square.

    Methods:
    - __init__(self, size=0): Initializes a Square object.
    - size: Getter method for the size attribute.
    - size.setter: Setter method for the size attribute.
    - area(self): Calculates and returns the area of the square.
    - __eq__(self, other): Implements the == operator.
    - __ne__(self, other): Implements the != operator.
    - __gt__(self, other): Implements the > operator.
    - __ge__(self, other): Implements the >= operator.
    - __lt__(self, other): Implements the < operator.
    - __le__(self, other): Implements the <= operator.
    """

    def __init__(self, size=0):
        """
        Initialize a Square.

        Args:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
        - value (int): The new size value.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """
        Implements the == operator.

        Args:
        - other: The other object to compare.

        Returns:
        - bool: True if both objects have the same area, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Implements the != operator.

        Args:
        - other: The other object to compare.

        Returns:
        - bool: True if both objects have different areas, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Implements the > operator.

        Args:
        - other: The other object to compare.

        Returns:
        - bool: True if the area of self is greater than the area of other,
                False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        raise TypeError("unsupported operand type(s) for >: 'Square'"
                        "and '{}'".format(type(other)))

    def __ge__(self, other):
        """
        Implements the >= operator.

        Args:
        - other: The other object to compare.

        Returns:
        - bool: True if the area of self is greater than or equal to the area
                of other, False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Implementing the < operator.

        Args:
        - other: The other object to compare.

        Returns:
        - bool: True if the area of self is less than the area of other,
                False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError("unsupported operand type(s) for <: 'Square'"
                        "and '{}'".format(type(other)))

    def __le__(self, other):
        """
        Implements the <= operator.

        Args:
        - other: The other object to compare.

        Returns:
        - bool: True if the area of self is less than or equal to
                the area of other, False otherwise.
        """
        return self.__lt__(other) or self.__eq__(other)
