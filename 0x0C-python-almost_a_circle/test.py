from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

"""Checks the create method."""
input = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
expected = Rectangle.create(**input)
print(expected.to_dictionary())
