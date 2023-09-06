#!/usr/bin/python3
""" This module adds two integers """


def add_integer(a, b=98):
    """ This function adds two integers
    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        int: sum of a and b
    Raises:
        TypeError: if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
