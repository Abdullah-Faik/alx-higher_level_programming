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
        self.assertEqual(self.sqaure.size, 13)

    def test_str(self):
        Base.reset()
        """Checks the __str__ method."""
        self.sqaure = Square(1, 2, 3, 4)
        self.assertEqual(str(self.sqaure), "[Square] (4) 2/3 - 1")

    def test_size(self):
        """Checks the size attribute."""
        self.sqaure = Square(1)
        self.assertIs(hasattr(self.sqaure, "size"), True)

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

    def test_to_json_empty(self):
        """Checks the json represntation with an empty list."""
        input = []
        expected = "[]"
        self.assertEqual(Base.to_json_string(input), expected)

    def test_to_json_none(self):
        """Checks the json represntation with None."""
        input = None
        expected = "[]"
        self.assertEqual(Base.to_json_string(input), expected)

    def test_create_Square(self):
        """Checks the create method."""
        self.sqaure = Square(1, 2)
        self.assertEqual(self.sqaure.x, 2)

    def test_create_Square(self):
        """Checks the create method."""
        self.sqaure = Square(1, 2, 3)
        self.assertEqual(self.sqaure.y, 3)

    def test_create_Square(self):
        """Checks the create method."""
        self.sqaure = Square(1, 2, 3, 4)
        self.assertEqual(self.sqaure.id, 4)

    def test_size_string(self):
        """Checks the size attribute."""
        with self.assertRaises(TypeError):
            self.sqaure = Square("1")

    def test_size_negative(self):
        """Checks the size attribute."""
        with self.assertRaises(ValueError):
            self.sqaure = Square(-1)

    def test_x_string(self):
        """Checks the size attribute."""
        with self.assertRaises(TypeError):
            self.sqaure = Square(1, "1")

    def test_x_negative(self):
        """Checks the size attribute."""
        with self.assertRaises(ValueError):
            self.sqaure = Square(1, -1)

    def test_y_string(self):
        """Checks the size attribute."""
        with self.assertRaises(TypeError):
            self.sqaure = Square(1, 1, "1")

    def test_y_negative(self):
        """Checks the size attribute."""
        with self.assertRaises(ValueError):
            self.sqaure = Square(1, 1, -1)

    def test_size_zero(self):
        """Checks the size attribute."""
        with self.assertRaises(ValueError):
            self.sqaure = Square(0)

    def test_create(self):
        """Test create method."""
        r1 = Square(3, 5, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())

    def test_1_create(self):
        """Test create method."""
        r2 = Square.create(**{'id': 89})
        self.assertEqual(r2.__str__(), "[Square] (89) 0/0 - 1")

    def test_2_create(self):
        """Test create method."""
        r2 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(r2.__str__(), "[Square] (89) 0/0 - 1")

    def test_3_create(self):
        """Test create method."""
        r2 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(r2.__str__(), "[Square] (89) 2/0 - 1")

    def test_4_create(self):
        """Test create method."""
        r2 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(r2.__str__(), "[Square] (89) 2/3 - 1")

    def test_save_to_file(self):
        """Test save_to_file method."""
        r1 = Square(10, 7, 2, 8)
        r2 = Square(2, 4, 0, 0)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 77)

    def test_save_to_file_None(self):
        """Test save_to_file method."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 2)

    def test_save_to_file_empty(self):
        """Test save_to_file method."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(len(f.read()), 2)
