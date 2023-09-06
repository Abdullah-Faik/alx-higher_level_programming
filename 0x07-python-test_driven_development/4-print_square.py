#!/usr/bin/python3
""" This module prints a square with the character # """


def print_square(size):
    """ This function prints a square with the character #
    Args:
        size (int): size of the square
    Returns:
        None
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be greater than or equal to 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
