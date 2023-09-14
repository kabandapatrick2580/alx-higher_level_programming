#!/usr/bin/python3
"""Adding a new attribute to an object."""


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if possible.

    If the object cannot have new attributes, raise a TypeError.

    Args:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Cannot add a new attribute to this object.")
    setattr(obj, attr_name, attr_value)
