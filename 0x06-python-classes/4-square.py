#!/usr/bin/python3
"""class definition"""


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
    """

    def __init__(self, size=0):
        """
        Initialization of a Square.

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
        to make size attr changeable outside the class

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
