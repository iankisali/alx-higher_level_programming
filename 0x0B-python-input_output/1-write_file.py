#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write string to UTF file
    Args:
        filename(string): name of file to write to
        text(string): text to write to file
    Return:
        number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as fl:
        return fl.write(text)
