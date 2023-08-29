#!/usr/bin/python3
"""Square class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """__init__ method.
        Args:
            size (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """size getter.
        Returns:
            size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter.
        Args:
            value (int): size value to be setted.
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        Returns:
            None.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
