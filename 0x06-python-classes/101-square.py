#!/usr/bin/python3

"""The definition of a Square class."""


class Square:
    """
    Representation a square.

    Attributes:
    - __size (int): The size of the square.
    - __position (tuple): The position of the square.

    Methods:
    - __init__(self, size=0, position=(0, 0)): Initializes a Square object.
    - area(self): Calculates and returns the area of the square.
    - my_print(self): Prints the square using '#' based on the size and
                      position of the square.
    - __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization a Square object.

        Args:
        - size (int): The size of the square.
        - position (tuple): The position of the square as a tuple of
                            two positive integers (x, y).

        Raises:
        - TypeError: If size is not an integer, or if position is not a
                     tuple of two positive integers.
        - ValueError: If size is less than 0, or if position contains
                      negative integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
        - tuple: The position of the square as a tuple of
                 two positive integers (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
        - value (tuple): The new position value as a tuple of two positive
                         integers (x, y).

        Raises:
        - TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise TypeError("position must be a tuple of "
                            "two positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' based on the size and position of
        the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - str: The string representation of the square.
        """
        if self.__size == 0:
            return ""
        else:
            sqr_lines = []
            for _ in range(self.__position[1]):
                sqr_lines.append("\n")
            for _ in range(self.__size):
                sqr_lines.append(" " * self.__position[0] + "#" * self.__size)
            return "\n".join(sqr_lines)
