#!/usr/bin/python3


class MyList(list):
    """A subclass of list that provides additional functionality."""

    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)
