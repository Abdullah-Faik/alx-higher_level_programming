#!/usr/bin/python3
""" add attribute"""


def add_attribute(obj, name, value):
    """ add attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
