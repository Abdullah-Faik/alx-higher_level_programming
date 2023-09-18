#!/usr/bin/python3
""" rectangle file """

from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init of the class"""
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
        """width"""
        return self.__width

    @width.setter
    def width(self, val):
        """set width"""
        self.int_validate("width", val)
        self.__width = val

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.int_validate("height", height)
        self.__height = height

    @property
    def x(self):
        """return x"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.position_validate("x", x)
        self.__x = x

    @property
    def y(self):
        """return y"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.position_validate("y", y)
        self.__y = y

    def area(self):
        """return area"""
        return self.__width * self.__height

    def display(self):
        """print rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """up the rectangle"""
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
        """return str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def int_validate(self, name, val):
        """validates if the value is an int"""
        if type(val) is not int:
            raise TypeError("{} must be an integer".format(name))
        if val <= 0:
            raise ValueError("{} must be > 0".format(name))

    def position_validate(self, name, val):
        if type(val) is not int:
            raise TypeError("{} must be a int".format(name))
        if val < 0:
            raise ValueError("{} must be >= 0".format(name))
