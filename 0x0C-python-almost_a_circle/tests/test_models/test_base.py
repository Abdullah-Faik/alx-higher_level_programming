#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class BaseTest(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Initializes the __nb_objects attribute before each test."""
        self.assertIs(hasattr(Base, "_Base__nb_objects"), True)
        Base._Base__nb_objects = 0

    def test_id_type(self):
        """Checks if the id is an integer type."""
        my_class = Base()
        self.assertIs(type(my_class.id), int)

    def test_id_increments(self):
        """Checks if the ids increment."""
        for i in range(1, 6):
            with self.subTest(i=i):
                my_class = Base()
                self.assertEqual(my_class.id, i)

    def test_sets_id(self):
        """Checks if the id can be set."""
        my_class = Base(13)
        self.assertEqual(my_class.id, 13)

    def test_sets_id_increments(self):
        """Checks if the ids increment after setting an id."""
        for i in range(1, 10):
            with self.subTest(i=i):
                if i == 5:
                    my_class = Base(13)
                    self.assertEqual(my_class.id, 13)
                else:
                    my_class = Base()
                    if i < 5:
                        self.assertEqual(my_class.id, i)
                    else:
                        self.assertEqual(my_class.id, i - 1)

    def test_sets_negative_id(self):
        """Checks if the id can be set with a negative integer."""
        my_class = Base(-7)
        self.assertEqual(my_class.id, -7)

    def test_sets_negative_id(self):
        """Checks if the id can be set with a negative integer."""
        my_class = Base(-7)
        self.assertEqual(my_class.id, -7)

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

    def test_to_json_string(self):
        """
        Test to_json_string
        """
        jstr = Base.to_json_string(
            [{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]
        )
        self.assertEqual(
            jstr, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        )
        jstr = Base.to_json_string(None)
        self.assertEqual(jstr, "[]")
        jstr = Base.to_json_string([])
        self.assertEqual(jstr, "[]")

    def test_from_json_string(self):
        """ Test from_json_string """
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])

    def test_create(self):
        """ Test create """
        r1 = Rectangle(3, 5, 1, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        """ Test load_from_file """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_output, [r1, r2])
        self.assertEqual(
            [i.to_dictionary() for i in list_rectangles_output],
            [r1.to_dictionary(), r2.to_dictionary()]
        )
        Rectangle.save_to_file(None)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])
        Rectangle.save_to_file([])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [])

    def test_save_to_file(self):
        """ Test save_to_file """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(
                json.loads(f.read()),
                [r1.to_dictionary(), r2.to_dictionary()]
            )
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [])
