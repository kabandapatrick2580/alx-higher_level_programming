#!/usr/bin/python3
"""class inheritance"""
from models.base import Base


class Rectangle(Base):
    """Child class Rectangle inherited from Super class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing constructors
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: size of the rectangle
            y: y size of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if id is None:
            super().__init__()
        else:
            self.id = id

    @property
    def width(self):
        """initialization of width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """initialization width setter
        Args"
            value: size of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """initialization of height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """initialization of height setter
        Args"
            value: size of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """initialization of x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """initialization of x setter
        Args"
            value: size of x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """initialization of y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """initialization of y setter
        Args"
            value: size of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """initialization of rectangle area"""
        return self.__width * self.__height

    def display(self):
        """display of rectangle elements"""
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")

            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returning string of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """updating arguments of the rectangle
        Args:
            *args: non keyworded arguments
            **kwargs: keyworded arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returning the dictionary set elements"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
