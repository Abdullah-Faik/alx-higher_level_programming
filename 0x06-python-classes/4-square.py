#!/usr/bin/python3
"""Square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """__init__ method.
        Args:
            size (int): size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area method.
        Returns:
            the area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """size getter.
        Returns:
            the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter.
        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
