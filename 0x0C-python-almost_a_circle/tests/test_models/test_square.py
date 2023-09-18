#!/usr/bin/python3
"""Unittest for the Square class."""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Square_0_Test(unittest.TestCase):
    """tests for the Square class."""

    def setUpClass():
        """set up class"""
        Base.reset()

    def setUp(self) -> None:
        """set up"""
        self.sqaure = None

    def tearDown(self) -> None:
        """tear down"""
        self.sqaure = None

    def test_id_type(self):
        """Checks if the id is an integer type."""
        self.sqaure = Square(1)
        self.assertIs(type(self.sqaure.id), int)

    def test_id_increments(self):
        """Checks if the ids increment."""
        Base.reset()
        for i in range(1, 6):
            with self.subTest(i=i):
                self.sqaure = Square(1)
                self.assertEqual(self.sqaure.id, i)

    def test_sets_id(self):
        """Checks if the id can be set."""
        self.sqaure = Square(13)
        self.assertEqual(self.sqaure.id, 13)

    def test_str(self):
        Base.reset()
        """Checks the __str__ method."""
        self.sqaure = Square(1, 2, 3, 4)
        self.assertEqual(str(self.sqaure), "[Square] (4) 2/3 - 1")

    def test_size(self):
        """Checks the size attribute."""
        self.sqaure = Square(1)
        self.assertIs(hasattr(self.sqaure, "size"), True)

    def test_size_private(self):
        """Checks if the size attribute is private."""
        self.sqaure = Square(1)
        with self.assertRaises(AttributeError):
            self.sqaure.size = 5

    def test_size_getter(self):
        """Checks the getter for the size attribute."""
        self.sqaure = Square(1)
        self.assertEqual(self.sqaure.size, 1)

    def test_size_setter(self):
        """Checks the setter for the size attribute."""
        self.sqaure = Square(1)
        self.sqaure.size = 5
        self.assertEqual(self.sqaure.size, 5)

    def test_update(self):
        """Checks the update method."""
        self.sqaure = Square(1)
        self.sqaure.update(5)
        self.assertEqual(self.sqaure.id, 5)

    def test_update_1(self):
        """Checks the update method."""
        self.sqaure = Square(1)
        self.sqaure.update(5, 5)
        self.assertEqual(self.sqaure.id, 5)
        self.assertEqual(self.sqaure.size, 5)

    def test_kwargs(self):
        """Checks the update method with kwargs."""
        self.sqaure = Square(1)
        self.sqaure.update(id=5)
        self.assertEqual(self.sqaure.id, 5)

    def test_to_dictionary(self):
        """Checks the to_dictionary method."""
        self.sqaure = Square(1, 2, 3, 4)
        self.assertEqual(self.sqaure.to_dictionary(),
                         {"id": 4, "size": 1, "x": 2, "y": 3})
        
    def test_to_json(self):
        """Checks the json represntation."""
        input = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        expected = json.dumps(input)
        self.assertEqual(Base.to_json_string(input), expected)
        
