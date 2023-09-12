#!/usr/bin/python3
"""A class MyList that inherits from the built-in list class."""


class MyList(list):
    """A subclass of the list class."""

    def print_sorted(self):
        """Prints the sorted elements of the list."""
        
        sorted_list = sorted(self)
        print(sorted_list)
