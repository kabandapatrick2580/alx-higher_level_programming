#!/usr/bin/python3
"""3-is_kind_class module"""


def is_kind_of_class(obj, a_class):
    """
    Description: Check if an object is an instance
    of a class or inherited from, a given class.

    Args:
    obj: object to be compared
    a_class: a class ti be compared
    Return: True if it belongs to a classor subclass, False Otherwise
    """

    if isinstance(obj, a_class):
        return True

    for base_class in obj.__class__.__bases__:
        if is_kind_of_class(base_class(), a_class):
            return True
        return False
