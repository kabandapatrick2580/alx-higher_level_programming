#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a given class."""
    
    if isinstance(obj, a_class):
        return True

    for base_class in obj.__class__.__bases__:
        if is_kind_of_class(base_class(), a_class):
            return True
        return False
