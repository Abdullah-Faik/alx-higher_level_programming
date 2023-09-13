#!/usr/bin/python3
""" class square"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
