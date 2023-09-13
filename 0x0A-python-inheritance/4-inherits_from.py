#!/usr/bin/python3
"""check if object is istance from class"""


def inherits_from(obj, a_class):
    """check if object is istance from class"""
    if isinstance(obj, a_class.super()):
        return True
    return False
