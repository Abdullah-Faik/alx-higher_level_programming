#!/usr/bin/python3
"""return dict of class"""


def class_to_json(obj):
    """ return json of the class"""
    return obj.__dict__
