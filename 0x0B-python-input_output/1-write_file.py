#!/usr/bin/python3
"""write text in file"""


def write_file(filename="", text=""):
    """ write to file
    Args:
        filename: file name
        text: text to write
    Return: number of characters written
    """
    with open(file=filename, mode="w", encoding="utf-8") as f:
        written = f.write(text)
        f.close()
    return written
