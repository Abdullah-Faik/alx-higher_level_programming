#!/usr/bin/python3
"""the file to read and print file data"""


def read_file(filename=""):
    """
    read file nad print it

    Args: file name
    Return: None
    """
    if (type(filename)is not str):
        return
    with open(file=filename, mode="r", encoding="utf-8") as f:
        print(f.read())

read_file(".gitignore")