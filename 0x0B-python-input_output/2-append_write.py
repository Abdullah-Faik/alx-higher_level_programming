#!/usr/bin/python3
"""append text in file"""


def append_write(filename="", text=""):
    """ append to file
    Args:
        filename: file name
        text: text to write
    Return: number of characters written
    """
    with open(file=filename, mode="a", encoding="utf-8") as f:
        bit = f.write(text)
        f.close()
    return bit
