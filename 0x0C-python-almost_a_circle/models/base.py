#!/usr/bin/python3
"""clss base for project"""


class Base:
    """basic class for python"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        self.id = None
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
