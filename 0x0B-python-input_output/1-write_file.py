#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write contents to the file.

    Args:
    filename(str): The name of the file.
    text(str): the content to be written in a file.
    Return: the number of characters writen in the file.
    """
    with open(filename, 'w', encoding='utf-8') as file_name:
        return file_name.write(text)
