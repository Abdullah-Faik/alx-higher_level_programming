#!/usr/bin/python3
"""check if object is istance from class"""


def inherits_from(obj, a_class):
    """check if object is istance from class"""
    if isinstance(obj, a_class.__bases__):
        return True
    return False
