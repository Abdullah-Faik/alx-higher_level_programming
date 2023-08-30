#!/usr/bin/python3
"""Square class"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.
        Args:
            size (int): size of the square.
        """
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
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

    def __str__(self):
        """__str__ method.
        Returns:
            string
        """
        if self.__size == 0:
            return ""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print()
        return ""
