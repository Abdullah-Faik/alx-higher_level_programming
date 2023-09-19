# /usr/bin/python3
"""Unittest for rectangle.py"""

import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class Test_0_RectangleID(unittest.TestCase):
    """Test cases for the 'id' attribute of Rectangle."""
    @classmethod
    def setUpClass(cls):
        """Common setup code that runs before each test."""
        Base.reset()

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_id_for_default(self):
        """Test the 'id' attribute for the default case."""
        self.rectangle = Rectangle(10, 2)
        self.assertEqual(self.rectangle.id, 1)

    def test_id_for_positive_id(self):
        """Test the 'id' attribute for a positive id."""
        self.rectangle = Rectangle(2, 10)
        self.assertEqual(self.rectangle.id, 2)

    def test_id_for_custom_id(self):
        """Test the 'id' attribute for a custom id."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.rectangle.id, 12)

    def test_id_for_negative_id(self):
        """Test the 'id' attribute for a negative id."""
        self.rectangle = Rectangle(10, 2, 0, 0, -1)
        self.assertEqual(self.rectangle.id, -1)

    def test_id_for_zero_id(self):
        """Test the 'id' attribute for an id of zero."""
        self.rectangle = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(self.rectangle.id, 0)

    def test_id_for_float_id(self):
        """Test the 'id' attribute for a float id."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        self.assertEqual(self.rectangle.id, 12.5)

    def test_id_for_string_id(self):
        """Test the 'id' attribute for a string id."""
        self.rectangle = Rectangle(10, 2, 0, 0, "string")
        self.assertEqual(self.rectangle.id, "string")


class Test_1_RectangleWidth (unittest.TestCase):
    def setUp(self):
        """ Common setup code that runs before each test"""
        self.rectangle = None

    def tearDown(self):
        """ Common cleanup code that runs after each test"""
        self.rectangle = None

    def test_initial_width(self):
        """ Test that the width is set correctly during initialization"""
        self.rectangle = Rectangle(10, 2)
        self.assertEqual(self.rectangle.width, 10)

    def test_set_valid_width(self):
        """ Test setting a valid width """
        self.rectangle = Rectangle(2, 10)
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

    def test_set_invalid_width_string(self):
        """ Test setting an invalid width with a string"""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = "5.5"

    def test_set_invalid_width_negative(self):
        """ Test setting an invalid negative width """
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            self.rectangle.width = -10

    def test_set_invalid_width_zero(self):
        """ Test setting an invalid width of zero """
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

    def test_set_invalid_width_other_types(self):
        """ Test setting invalid width with various non-integer types"""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = "string"
        with self.assertRaises(TypeError):
            self.rectangle.width = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.rectangle.width = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.rectangle.width = {1, 2, 3}
        with self.assertRaises(TypeError):
            self.rectangle.width = {"a": 1, "b": 2, "c": 3}

    def test_set_width_to_none(self):
        """ Test setting width to None"""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = None
        
    def test_set_width_with_string(self):
        """ Test setting width with string"""
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle("1", 2)
        
    def test_set_width_with_float(self):
        """ Test setting width with float"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = "1"
        
    def test_set_width_with_negative(self):
        """ Test setting width with negative"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            self.rectangle.width = -1
    
    def test_set_width_with_negative_1(self):
        """ Test setting width with zero"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(-1, 2)


class Test_2_RectangleHeight(unittest.TestCase):
    """Test cases for the 'width' attribute of Rectangle."""

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_initial_width(self):
        """Test that the width is set correctly during initialization."""
        self.rectangle = Rectangle(10, 2)
        self.assertEqual(self.rectangle.width, 10)

    def test_set_valid_width(self):
        """Test setting a valid width."""
        self.rectangle = Rectangle(2, 10)
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

    def test_set_invalid_width_string(self):
        """Test setting an invalid width with a string."""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = "5.5"

    def test_set_invalid_width_negative(self):
        """Test setting an invalid negative width."""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            self.rectangle.width = -10

    def test_set_invalid_width_zero(self):
        """Test setting an invalid width of zero."""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

    def test_set_invalid_width_other_types(self):
        """Test setting invalid width with various non-integer types."""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = "string"
        with self.assertRaises(TypeError):
            self.rectangle.width = [1, 2, 3]
        with self.assertRaises(TypeError):
            self.rectangle.width = (1, 2, 3)
        with self.assertRaises(TypeError):
            self.rectangle.width = {1, 2, 3}
        with self.assertRaises(TypeError):
            self.rectangle.width = {"a": 1, "b": 2, "c": 3}

    def test_set_width_to_none(self):
        """Test setting width to None."""
        self.rectangle = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            self.rectangle.width = None

    def test_set_width_with_string(self):
        """ Test setting width with string"""
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(1, "2")
        
    def test_set_width_with_float(self):
        """ Test setting width with float"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.rectangle.height = "1"
        
    def test_set_width_with_negative(self):
        """ Test setting width with negative"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            self.rectangle.height = -1
    
    def test_set_width_with_negative_1(self):
        """ Test setting width with zero"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(1, -2)
        
    def test_Set_width_With_zero(self):
        """test seeting width with zero"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(0, 1)
    
    def test_Set_height_With_zero(self):
        """test seeting width with zero"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(1, 0)


class Test_3_RectangleX(unittest.TestCase):
    """Test cases for the 'x' attribute of Rectangle."""

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_x_for_default(self):
        """Test the 'x' attribute for the default case."""
        self.rectangle = Rectangle(10, 2)
        self.assertEqual(self.rectangle.x, 0)

    def test_x_for_positive_x(self):
        """Test the 'x' attribute for a positive x value."""
        self.rectangle = Rectangle(2, 10)
        self.assertEqual(self.rectangle.x, 0)

    def test_x_for_custom_x(self):
        """Test the 'x' attribute for a custom x value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.rectangle.x, 0)

    def test_x_for_negative_x(self):
        """Test the 'x' attribute for a negative x value."""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, 2, -1, 0)

    def test_x_for_setterself(self):
        """Test the 'x' attribute for a negative x value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 0)
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

    def test_x_for_negative_x_on_creation(self):
        """Test creating a Rectangle with a negative x value."""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, 2, -10, 0)

    def test_x_for_float_x(self):
        """Test the 'x' attribute for a float x value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        self.assertEqual(self.rectangle.x, 0)

    def test_x_for_float_x_on_set(self):
        """Test setting the 'x' attribute to a float value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = 5.5

    def test_x_for_string_x_on_set(self):
        """Test setting the 'x' attribute to a string value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = "string"

    def test_x_for_list_x_on_set(self):
        """Test setting the 'x' attribute to a list value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = [1, 2, 3]

    def test_x_for_tuple_x_on_set(self):
        """Test setting the 'x' attribute to a tuple value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = (1, 2, 3)

    def test_x_for_set_x_on_set(self):
        """Test setting the 'x' attribute to a set value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = {1, 2, 3}

    def test_x_for_dict_x_on_set(self):
        """Test setting the 'x' attribute to a dictionary value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = {"a": 1, "b": 2, "c": 3}

    def test_x_for_none_x_on_set(self):
        """Test setting the 'x' attribute to None."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.x = None

    def test_set_x_with_string(self):
        """ Test setting width with string"""
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(1, 2, "3")
        
    def test_set_x_with_float(self):
        """ Test setting width with float"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.rectangle.x = "1"
        
    def test_set_x_with_negative(self):
        """ Test setting width with negative"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            self.rectangle.x= -1
    
    def test_set_x_with_negative_1(self):
        """ Test setting width with zero"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(1, 2,-1)


class Test_4_RectangleY(unittest.TestCase):
    """Test cases for the 'y' attribute of Rectangle."""

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_y_for_default(self):
        """Test the 'y' attribute for the default case."""
        self.rectangle = Rectangle(10, 2)
        self.assertEqual(self.rectangle.y, 0)

    def test_y_for_positive_y(self):
        """Test the 'y' attribute for a positive y value."""
        self.rectangle = Rectangle(2, 10)
        self.assertEqual(self.rectangle.y, 0)

    def test_y_for_custom_y(self):
        """Test the 'y' attribute for a custom y value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.rectangle.y, 0)

    def test_y_for_negative_y(self):
        """Test the 'y' attribute for a negative y value."""
        self.rectangle = Rectangle(10, 2, 0, 0)
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_y_for_setterself(self):
        """Test the 'y' attribute for a negative y value."""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, -2, 0, 0, 0)

    def test_y_for_negative_y_on_creation(self):
        """Test creating a Rectangle with a negative y value."""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, 2, 0, -10)

    def test_y_for_float_y(self):
        """Test the 'y' attribute for a float y value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        self.assertEqual(self.rectangle.y, 0)

    def test_y_for_float_y_on_set(self):
        """Test setting the 'y' attribute to a float value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = 5.5

    def test_y_for_string_y_on_set(self):
        """Test setting the 'y' attribute to a string value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = "string"

    def test_y_for_list_y_on_set(self):
        """Test setting the 'y' attribute to a list value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = [1, 2, 3]

    def test_y_for_tuple_y_on_set(self):
        """Test setting the 'y' attribute to a tuple value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = (1, 2, 3)

    def test_y_for_set_y_on_set(self):
        """Test setting the 'y' attribute to a set value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = {1, 2, 3}

    def test_y_for_dict_y_on_set(self):
        """Test setting the 'y' attribute to a dictionary value."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = {"a": 1, "b": 2, "c": 3}

    def test_y_for_none_y_on_set(self):
        """Test setting the 'y' attribute to None."""
        self.rectangle = Rectangle(10, 2, 0, 0, 12.5)
        with self.assertRaises(TypeError):
            self.rectangle.y = None
    
    def test_set_y_with_string(self):
        """ Test setting width with string"""
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(1, 2, 3, "4")
        
    def test_set_y_with_float(self):
        """ Test setting width with float"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.rectangle.y = "1"
    
    def test_set_y_with_negative_0(self):
        """ Test setting width with negative"""
        self.rectangle = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            self.rectangle.y = -1
    
    def test_set_y_with_negative_1(self):
        """ Test setting width with zero"""
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(1, 2, 3, -4)


class Test_5_RectangleArea(unittest.TestCase):
    """Test cases for the 'area' method of Rectangle."""

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_area_for_default(self):
        """Test the 'area' method for the default case."""
        self.rectangle = Rectangle(10, 2)
        self.assertEqual(self.rectangle.area(), 20)

    def test_area_for_full_rectangle(self):
        """Test the 'area' method for a full rectangle."""
        self.rectangle = Rectangle(5, 5, 1, 1, 1)
        self.assertEqual(self.rectangle.area(), 25)


class Test_6_RectangleDisplay(unittest.TestCase):
    """Test cases for the 'display' method of Rectangle."""

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_display_for_default(self):
        """Test the 'display' method for the default case."""
        self.rectangle = Rectangle(2, 2)
        sdtout = StringIO()
        with patch('sys.stdout', new=sdtout) as fake_out:
            self.rectangle.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")

    def test_display_for_full_rectangle(self):
        """Test the 'display' method for a full rectangle."""
        self.rectangle = Rectangle(5, 5, 1, 1, 1)
        sdtout = StringIO()
        with patch('sys.stdout', new=sdtout) as fake_out:
            self.rectangle.display()
            self.assertEqual(fake_out.getvalue(),
                             "\n #####\n #####\n #####\n #####\n #####\n")


class Test_7_RectangleStr(unittest.TestCase):
    """Test cases for the '__str__' method of Rectangle."""

    @classmethod
    def setUpClass(cls):
        """Common setup code that runs before each test."""
        Base.reset()

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_str_for_default(self):
        """Test the '__str__' method for the default case."""
        self.rectangle = Rectangle(4, 6)
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (1) 0/0 - 4/6")

    def test_str_for_full_rectangle(self):
        """Test the '__str__' method for a full rectangle."""
        self.rectangle = Rectangle(5, 5, 1, 1)
        self.assertEqual(self.rectangle.__str__(), "[Rectangle] (2) 1/1 - 5/5")

    def test_str_for_custom_id(self):
        """Test the '__str__' method for a custom id."""
        self.rectangle = Rectangle(5, 5, 1, 1, 12)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (12) 1/1 - 5/5")


class Test_8_RectangleUpdate(unittest.TestCase):
    """Test cases for the 'update' method of Rectangle."""

    @classmethod
    def setUpClass(cls):
        """Common setup code that runs before each test."""
        Base.reset()

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None
        Test_8_RectangleUpdate.setUpClass()

    def tearDown(self):
        """Common cleanup code that runs after each test."""
        self.rectangle = None

    def test_0_update_for_default(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update()
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (1) 10/10 - 10/10")

    def test_update_for_args(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(89)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 10/10 - 10/10")

    def test_update_for_args_2(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(89, 2)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 10/10 - 2/10")

    def test_update_for_args_3(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(89, 2, 3)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 10/10 - 2/3")

    def test_update_for_args_4(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(89, 2, 3, 4)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 4/10 - 2/3")

    def test_update_for_args_5(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 4/5 - 2/3")

    def test_update_for_unvalid_valus(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            self.rectangle.update(89, -1)

        with self.assertRaises(ValueError):
            self.rectangle.update(89, 1, -1)

        with self.assertRaises(ValueError):
            self.rectangle.update(89, 1, 1, -1)

        with self.assertRaises(ValueError):
            self.rectangle.update(89, 1, 1, 1, -1)

        with self.assertRaises(TypeError):
            self.rectangle.update(89, "string")

        with self.assertRaises(TypeError):
            self.rectangle.update(89, 1, "string")

        with self.assertRaises(TypeError):
            self.rectangle.update(89, 1, 1, "string")

        with self.assertRaises(TypeError):
            self.rectangle.update(89, 1, 1, 1, "string")

    def test_update_for_kwargs_0(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(id=89)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 10/10 - 10/10")

    def test_update_for_kwargs_1(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(width=1)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (1) 10/10 - 1/10")

    def test_update_for_kwargs_2(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(height=1)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (1) 10/10 - 10/1")

    def test_update_for_kwargs_3(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(x=1)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (1) 1/10 - 10/10")

    def test_update_for_kwargs_4(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        self.rectangle.update(y=1)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (1) 10/1 - 10/10")

    def test_update_for_kwargs_5_unvalid(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            self.rectangle.update(width="string")

        with self.assertRaises(TypeError):
            self.rectangle.update(height="string")

        with self.assertRaises(TypeError):
            self.rectangle.update(x="string")

        with self.assertRaises(TypeError):
            self.rectangle.update(y="string")

        with self.assertRaises(ValueError):
            self.rectangle.update(width=-1)

        with self.assertRaises(ValueError):
            self.rectangle.update(height=-1)

        with self.assertRaises(ValueError):
            self.rectangle.update(x=-1)

        with self.assertRaises(ValueError):
            self.rectangle.update(y=-1)

    def test_update_for_kwargs_6(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10, 10)
        self.rectangle.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(self.rectangle.__str__(),
                         "[Rectangle] (89) 3/4 - 1/2")

    def test_dict(self):
        """Test the 'update' method for the default case."""
        self.rectangle = Rectangle(10, 10, 10, 10, 10)
        excepted = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.rectangle.update(**excepted)
        self.assertEqual(self.rectangle.to_dictionary(), excepted)


class Test_9_Baseother(unittest.TestCase):
    """Test cases for the  method of Base."""

    @classmethod
    def setUpClass(self):
        """Common setup code that runs before each test."""
        Base.reset()

    def setUp(self):
        """Common setup code that runs before each test."""
        self.rectangle = None
        Test_9_Baseother.setUpClass()

    def tearDown(self):
        self.rectangle = None

    def test_0_to_json(self):
        self.rectangle = Rectangle(10, 10, 10, 10, 10)
        q1 = self.rectangle.to_json_string([self.rectangle.to_dictionary()])
        self.assertEqual(type(q1), str)

    def test_1_to_json(self):
        self.rectangle = Rectangle(10, 10, 10, 10, 10)
        q1 = self.rectangle.to_json_string(None)
        self.assertEqual(q1, "[]")

    def test_2_to_json(self):
        self.rectangle = Rectangle(10, 10, 10, 10, 10)
        q1 = self.rectangle.to_json_string([])
        self.assertEqual(q1, "[]")

    def test_3_to_json(self):
        self.rectangle = Rectangle(10, 10)
        q1 = self.rectangle.to_json_string([self.rectangle.to_dictionary()])
        q2 = Base.to_json_string([self.rectangle.to_dictionary()])
        self.assertEqual(q1, q2)

    def test_4_to_json(self):
        self.rectangle = Rectangle(10, 10)
        q = {'id': 1, 'width': 10, 'height': 10, 'x': 0, 'y': 0}
        q1 = Base.to_json_string([q])
        self.assertNotEqual(q1, q)

