#!/usr/bin/python3
"""A module for adding items to a JSON file."""

import sys
import json

def save_to_json_file(data, filename):
    """Save data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_json_file(filename):
    """Load data from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
