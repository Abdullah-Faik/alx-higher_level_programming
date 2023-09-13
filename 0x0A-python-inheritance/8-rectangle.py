#!/usr/bin/python3
""" rectangle"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle task"""

    def __init__(self, width, height):
        if super().integer_validator("width", width):
            self.width = width
        if self.integer_validator("height", height):
            self.height = height
