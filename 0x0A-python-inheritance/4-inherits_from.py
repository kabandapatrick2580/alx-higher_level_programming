#!/usr/bin/python3


def inherits_from(obj, a_class):
    """Check if an object is an instance that inherits from a given class."""

    return issubclass(type(obj), a_class) and type(obj) != a_class
