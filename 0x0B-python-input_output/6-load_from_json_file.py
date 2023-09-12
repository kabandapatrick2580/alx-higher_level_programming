#!/usr/bin/python3
"""6-load_from_json_file."""


import json


def load_from_json_file(filename):
    """Create reliable object from json file."""
    with open(filename, 'r') as file:
        data = file.read()
        return json.loads(data)
