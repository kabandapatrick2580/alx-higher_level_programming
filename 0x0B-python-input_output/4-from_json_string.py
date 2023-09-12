#!/usr/bin/python3
"""4-from_json_string module."""


import json


def from_json_string(my_str):
    """Definition of the method.
    Description:
    This function converts Json into a
    python object.

    Args:
    my_str: a json string to be converted into a python object.
    Return: a python object.
    """
    return json.loads(my_str)
