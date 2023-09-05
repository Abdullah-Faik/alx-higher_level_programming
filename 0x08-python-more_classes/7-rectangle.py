#!/usr/bin/python3
"""Module 1-rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

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
    def height(self):
        """
        Retrieve height
        Args:
            None
        Return:
            self.__height
        """
        return self.__height

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

    def area(self):
        """
        area of rectangle
        Args:
            self.object
        Return:
            the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        perimeter of rectangle
        Args:
            self.object
        Return:
            the perimeter
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def print(self):
        """
        print square by '#'
        Args:
            self.object
        Return:
            None
        """
        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                print("")
        return ""

    def __str__(self):
        """
        print square by '#'
        Args:
            self.object
        Return:
            None
        """
        if (self.__width != 0 and self.__height != 0):
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                if i != self.__height - 1:
                    print("")
        return ""

    def __repr__(self):
        """
        respresent the class
        Args:
            self.object
        Return:
            a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        delete the class
        Args:
            self.object
        Return:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
