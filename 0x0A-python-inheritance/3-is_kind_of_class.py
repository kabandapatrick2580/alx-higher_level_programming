#!/usr/bin/python3
"""Check if an object is an instance of, or an instance of a class that inherits from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or an instance of a subclass."""

    return isinstance(obj, a_class)
