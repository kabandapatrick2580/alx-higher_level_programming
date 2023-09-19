#!/usr/bin/python3
"""the module for the square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Methods that return attributes
        Args:
            size: size of square
            x: x size
            y: y size
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """a Method that return string"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """Computing Getter size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """Computing Setter the size of the square
        Args:
            value: size of square
        Return:
            always nothing
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method for updating the size of the square
        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        Return:
            always nothing
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
