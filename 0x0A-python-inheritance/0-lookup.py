#!/usr/bin/python3
"""Defines object attributes and methods using the lookup function."""


def lookup(obj):
    """Returns a list of available attributes for the given object."""
    
    attr = dir(obj)
    return attr

