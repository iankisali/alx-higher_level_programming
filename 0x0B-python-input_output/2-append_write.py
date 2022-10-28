#!/usr/bin/python3
"""function that appends to a text file"""


def append_write(filename="", text=""):
    """Function that appends to a text file
    Args:
        filename(string): file name to append to
        text(string): text to append to filename
    Return:
        Number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as fn:
        return fn.write(text)
