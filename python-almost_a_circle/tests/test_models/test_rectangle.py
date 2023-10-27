#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest
import io
import sys


from tests.test_models.test_base import TestBase
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    # INHERITANCE
    def test_rectangle_inherits_from_base(self):
        """ Testing inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    # ATTRIBUTES
    def test_valid_attributes(self):
        """ Testing valid attributes """
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_invalid_width(self):
        """ Testing invalid width """
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle("hello", 20, 5, 5)

    def test_invalid_height(self):
        """ Testing invalid height """
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, None, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 5, 5)

    def test_invalid_x(self):
        """ Testing invalid x """
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, None, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "hello", 5)

    def test_invalid_y(self):
        """ Testing invalid y """
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, None)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "hello")

    # AREA
    def test_area(self):
        """ Testing area """
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.area(), 200)

    def test_area_large(self):
        """ Testing large area """
        rect = Rectangle(1000, 2000, 500, 500)
        self.assertEqual(rect.area(), 2000000)

    def test_area_zero(self):
        """ Testing zero area """
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0)

    def test_area_string(self):
        """ Testing string area """
        with self.assertRaises(TypeError):
            Rectangle("hello", 20, 0, 0)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 0, 0)

    def test_area_negative(self):
        """ Testing negative area """
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 0, 0)

    # DISPLAY
    def test_display(self):
        """ Testing display """
        rect = Rectangle(3, 2, 0, 0)
        expected_output = "###\n###"
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue().strip(), expected_output)

    def test_display_x_y(self):
        """ Testing display with x and y coordinates """
        rect = Rectangle(3, 2, 2, 1, 42)
        expected_output = '\n  ###\n  ###\n'
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_display_zero_x_y(self):
        """ Testing display with x and y coordinates """
        rect = Rectangle(3, 2, 0, 0, 99)
        expected_output = '###\n###\n'
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue(), expected_output)

    def test_display_large_x_y(self):
        """ Testing display with x and y coordinates """
        rect = Rectangle(2, 2, 5, 3, 10)
        expected_output = '\n\n\n     ##\n     ##\n'
        with io.StringIO() as output_buffer:
            sys.stdout = output_buffer
            rect.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(output_buffer.getvalue(), expected_output)

    # STRING REP
    def test_str_representation(self):
        """ Testing string rep """
        rect = Rectangle(5, 4, 1, 2, 42)
        expected_str = "[Rectangle] (42) 1/2 - 5/4"
        self.assertEqual(str(rect), expected_str)

    def test_str_representation_with_zero_coordinates(self):
        """ Testing string rep with zero coordinates """
        rect = Rectangle(3, 3, 0, 0, 99)
        expected_str = "[Rectangle] (99) 0/0 - 3/3"
        self.assertEqual(str(rect), expected_str)

    def test_str_representation_with_negative_id(self):
        """ Testing string rep with negative id """
        rect = Rectangle(2, 2, 2, 2, -1)
        expected_str = "[Rectangle] (-1) 2/2 - 2/2"
        self.assertEqual(str(rect), expected_str)

    # UPDATE
    def test_update_with_args(self):
        """ Testing update with args """
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update(1, 4, 3, 0, 0)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_update_incomplete_args(self):
        """ Testing update with incomplete args """
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update(1, 4, 3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_update_no_arguments(self):
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update()
        self.assertEqual(rect.id, 42)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_update_kwargs_only(self):
        """ Testing update with kwargs only """
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update(width=4, height=3, id=1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_update_args_and_kwargs_combined1(self):
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update(1, 4, height=3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_update_args_and_kwargs_combined2(self):
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update(1, 3, width=4, x=0)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    def test_update_unknown_attributes(self):
        rect = Rectangle(3, 2, 2, 1, 42)
        rect.update(1, width=4, depth=3)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 1)

    # DICTIONARY
    def test_to_dictionary(self):
        """ Testing to dictionary """
        rect = Rectangle(3, 2, 2, 1, 42)
        expected_dict = {'id': 42, 'width': 3, 'height': 2, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_zero_coordinates(self):
        """ Testing to dictionary with zero coordinates """
        rect = Rectangle(3, 2, 0, 0, 42)
        expected_dict = {'id': 42, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_negative_id(self):
        """ Testing to dictionary with negative id """
        rect = Rectangle(3, 2, 2, 1, -42)
        expected_dict = {'id': -42, 'width': 3, 'height': 2, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_string_id(self):
        """ Testing to dictionary with string id """
        rect = Rectangle(3, 2, 2, 1, "hello")
        expected_dict = {
            'id': "hello",
            'width': 3,
            'height': 2,
            'x': 2,
            'y': 1
        }
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_to_dictionary_empty_id(self):
        """ Testing to dictionary with empty ID """
        rect = Rectangle(3, 2, 2, 1, "")
        expected_dict = {'id': "", 'width': 3, 'height': 2, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
