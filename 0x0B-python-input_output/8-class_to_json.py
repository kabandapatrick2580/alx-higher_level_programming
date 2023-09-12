#!/usr/bin/python3
"""A module for converting Python objects to JSON-serializable dictionaries."""


def class_to_json(obj):
    """
    Convert an object to a dictionary representation for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the object with simple data structures
        (list, dictionary, string, integer, and boolean)
        suitable for JSON serialization.

    """
    if isinstance(obj, (list, dict, str, int, bool)):
        return obj
    elif isinstance(obj, (tuple, set)):
        return list(obj)
    elif isinstance(obj, object):
        json_dict = {}
        for attr in obj.__dict__:
            value = obj.__dict__[attr]
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[attr] = value
            elif isinstance(value, (tuple, set)):
                json_dict[attr] = list(value)
            elif isinstance(value, object):
                json_dict[attr] = class_to_json(value)
        return json_dict
