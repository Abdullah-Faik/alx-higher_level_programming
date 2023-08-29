#!/usr/bin/python3
"""Square class"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) is not tuple or len(position) != 2 and \
                type(position[0]) is not int and type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """position getter.
        Returns:
            the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter.
        Args:
            value (int): position of the square.
        """
        if type(value) is not tuple or len(value) != 2 and \
                type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """my_print method.
        Returns:
            square with the character
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
