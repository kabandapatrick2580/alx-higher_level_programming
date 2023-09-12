#!/usr/bin/python3
"""2-append_write module."""


def append_write(filename="", text=""):
    """Append contents to a file.

    Args:
    filename(str): name of the file.
    text(str): the text to be appended.
    Return: the number of characters appended.
    """
    with open(filename, 'a', encoding='utf-8') as file_name:
        return file_name.write(text)
