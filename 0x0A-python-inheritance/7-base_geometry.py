#!/usr/bin/python3
""" empty class"""


class BaseGeometry:
    """ empty class"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(str(name)+" must be an integer")
        if value <= 0:
            raise ValueError(str(name)+" must be greater than 0")
    
