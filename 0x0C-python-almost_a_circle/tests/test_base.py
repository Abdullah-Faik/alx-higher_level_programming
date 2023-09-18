#!/usr/bin/python3
"""Unittest for base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for base.py"""

    def test_id(self):
        """Test for id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base(-1)
        self.assertEqual(b5.id, -1)
        b6 = Base(0)
        self.assertEqual(b6.id, 0)
        b7 = Base(12)
        self.assertEqual(b7.id, 12)
        b8 = Base(12.5)
        self.assertEqual(b8.id, 12.5)
        b9 = Base("string")
        self.assertEqual(b9.id, "string")
        b10 = Base([1, 2, 3])
        self.assertEqual(b10.id, [1, 2, 3])
        b11 = Base((1, 2, 3))
        self.assertEqual(b11.id, (1, 2, 3))
        b12 = Base({1, 2, 3})
        self.assertEqual(b12.id, {1, 2, 3})
        b13 = Base({"a": 1, "b": 2, "c": 3})
        self.assertEqual(b13.id, {"a": 1, "b": 2, "c": 3})
        b14 = Base(None)
        self.assertEqual(b14.id, 4)

    def test_to_json_string(self):
        """Test for to_json_string method"""
        pass

    def test_save_to_file(self):
        """Test for save_to_file method"""
        pass

    def test_from_json_string(self):
        """Test for from_json_string method"""
        pass

    def test_create(self):
        """Test for create method"""
        pass

    def test_load_from_file(self):
        """Test for load_from_file method"""
        pass

if __name__ == '__main__':
    unittest.main()