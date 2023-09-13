#!/usr/bin/python3
"""Module that contains a function that
returns True if the object is exactly"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance of the class"""

    """
    Args:
        obj: object
        a_class: class
    Returns:
        True if the object is exactly an instance of the specified class
    """
    if obj is None or a_class is None:
        return False

    if type(obj) == a_class:
        return True
    else:
        return False
