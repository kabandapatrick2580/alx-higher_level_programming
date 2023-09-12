#!/usr/bin/python3
"""0-read_file module."""


def read_file(filename=""):
    """Read a text file."""
    with open(filename, 'r', encoding='utf-8') as file_name:
        for line in file_name:
            print(line, end="")
