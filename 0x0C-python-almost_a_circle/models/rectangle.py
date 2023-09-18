#!/usr/bin/python3
""" Rectangle class """

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle object"""
        super().__init__(id)
        self.int_validate("width", width)
        self.__width = width
        self.int_validate("height", height)
        self.__height = height
        self.position_validate("x", x)
        self.__x = x
        self.position_validate("y", y)
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, val):
        """Set the width of the rectangle"""
        self.int_validate("width", val)
        self.__width = val

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, val):
        """Set the height of the rectangle"""
        self.int_validate("height", val)
        self.__height = val

    @property
    def x(self):
        """Get the x-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, val):
        """Set the x-coordinate of the rectangle"""
        self.position_validate("x", val)
        self.__x = val

    @property
    def y(self):
        """Get the y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, val):
        """Set the y-coordinate of the rectangle"""
        self.position_validate("y", val)
        self.__y = val

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle using '#' characters"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def int_validate(self, property_name, value):
        """Validate that a property is an integer and > 0"""
        if not isinstance(value, int):
            raise TypeError(f"{property_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{property_name} must be > 0")

    def position_validate(self, property_name, value):
        """Validate that a position property is an integer and >= 0"""
        if not isinstance(value, int):
            raise TypeError(f"{property_name} must be an integer")
        if value < 0:
            raise ValueError(f"{property_name} must be >= 0")
