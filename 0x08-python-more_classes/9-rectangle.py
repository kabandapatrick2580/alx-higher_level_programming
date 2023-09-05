#!/usr/bin/python3

class Rectangle:
    """Represents a rectangle.

    Attributes:
        number_of_instances : The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0  # Class attribute to track the number of instances created.
    print_symbol = "#"  # Class attribute to determine the symbol used for string representation.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width  # Private attribute to store the width of the rectangle.
        self.__height = height  # Private attribute to store the height of the rectangle.
        Rectangle.number_of_instances += 1  # Increment class attribute to count instances.

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
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
        """Set the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
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
        """Return a string representation of the rectangle using the print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(
            [str(self.print_symbol) * self.__width] * self.__height
        )

    def __repr__(self):
        """
        Return a string representation of the Rectangle.

        This can be used to recreate a new instance.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message when an instance is deleted and decrement the class attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement class attribute when an instance is deleted.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)
