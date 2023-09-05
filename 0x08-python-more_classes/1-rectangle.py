#!/usr/bin/python3
"""Module 1-rectangle"""


from collections.abc import Iterable


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Retrieve width
        Args:
            None
        Return:
            self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set width
        Args:
            value: integer
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(Self):
        """
        Retrieve height
        Args:
            None
        Return:
            self.__height
        """
        return Self.__height

    @height.setter
    def height(self, value):
        """
        Set height
        Args:
            value: integer
        Return:
            None
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
