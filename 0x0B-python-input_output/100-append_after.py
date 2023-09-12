#!/usr/bin/python3
"""Module to append text after specific lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to find within the file.
        new_string (str): The string to insert after each found line.
    """
    if not filename or not search_string or not new_string:
        return

    with open(filename, 'r') as file:
        lines_list = file.readlines()

    updated_lines = []
    for line in lines_list:
        updated_lines.append(line)
        if search_string in line:
            updated_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(updated_lines)
