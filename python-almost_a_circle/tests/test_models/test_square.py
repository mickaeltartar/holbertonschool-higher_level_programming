#!/usr/bin/python3
""" Unittest for Square class """

import unittest
import os

from tests.test_models.test_rectangle import TestRectangle
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(TestRectangle):
    """ Testing Square Class """

    # INHERITANCE
    def test_square_inherits_from_rectangle(self):
        """ Testing inheritance """
        square = Square(5)
        self.assertTrue(isinstance(square, Rectangle),
                        "Square should inherit from Rectangle")

    # INIT
    def test_square_init(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_square(self):
        """ Testing square initialization """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    # STR REP
    def test_square_str_representation(self):
        """ Testing square string representation """
        square = Square(3, 1, 2, 42)
        self.assertEqual(str(square), "[Square] (42) 1/2 - 3")

    # SIZE VALIDATION
    def test_size_getter(self):
        """ Testing size getter """
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """ Testing size setter """
        square = Square(5, 2, 3, 1)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_size_setter_negative(self):
        """ Testing size setter with negative value """
        with self.assertRaises(ValueError):
            square = Square(5)
            square.size = -10

    def test_size_setter_zero(self):
        """ Testing size setter with zero value """
        with self.assertRaises(ValueError):
            square = Square(5, 2, 3, 1)
            square.size = 0

    def test_size_setter_float(self):
        """ Testing size setter with float value """
        with self.assertRaises(TypeError):
            square = Square(5, 2, 3, 1)
            square.size = 3.14

    def test_size_setter_string(self):
        """ Testing size setter with string value """
        with self.assertRaises(TypeError):
            square = Square(5, 2, 3, 1)
            square.size = "hello"

    def test_update_kwargs_only(self):
        """ Testing square initialization with kwargs """
        square = Square(3, 1, 2, 42)
        square.update(size=4, x=3, y=0, id=1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 0)

    def test_update_kwargs_args1(self):
        """ Testing square initialization with kwargs """
        square = Square(3, 1, 2, 42)
        square.update(1, 4, size=3)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_args_kwargs2(self):
        square = Square(3, 1, 2, 42)
        square.update(1, size=4, x=0)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

    def test_update_unknown_attributes(self):
        """ Testing update with unknown attributes """
        square = Square(3, 2, 4, 5)
        square.update(1, size=4, x=0)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 4)

    # DICTONARY

    def test_square_to_dictionary(self):
        """ Testing to_dictionary method of Square """
        square = Square(5, 2, 3, 1)
        dictionary = square.to_dictionary()
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3
        }
        self.assertEqual(dictionary, expected_dict)

    def test_square_dictionary(self):
        """ Testing square dictionary  """
        square = Square(3, 2, 4, 5)
        square_dictionary = square.to_dictionary()
        expected_dictionary = {'id': 5, 'size': 3, 'x': 2, 'y': 4}
        self.assertEqual(square_dictionary, expected_dictionary)

    def test_square_zero_coordinates(self):
        """ Testing to dictionary with zero coordinates """
        rect = Rectangle(3, 2, 0, 0, 42)
        expected_dict = {'id': 42, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_sqaure_to_dictionary_negative_id(self):
        """ Testing to dictionary with negative id """
        rect = Rectangle(3, 2, 2, 1, -42)
        expected_dict = {'id': -42, 'width': 3, 'height': 2, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    def test_square_to_dictionary_string_id(self):
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

    def test_square_to_dictionary_empty_id(self):
        """ Testing to dictionary with empty ID """
        rect = Rectangle(3, 2, 2, 1, "")
        expected_dict = {'id': "", 'width': 3, 'height': 2, 'x': 2, 'y': 1}
        self.assertEqual(rect.to_dictionary(), expected_dict)

    # NEW
    def test_square_with_width_and_height(self):
        square = Square(1, 2)
        self.assertIsInstance(square, Square)

    def test_square_with_width_height_and_x(self):
        square = Square(1, 2, 3)
        self.assertIsInstance(square, Square)

    def test_square_with_non_integer_width(self):
        with self.assertRaises(TypeError):
            square = Square("1")

    def test_square_with_non_integer_height(self):
        with self.assertRaises(TypeError):
            square = Square(1, "2")

    def test_square_with_non_integer_x(self):
        with self.assertRaises(TypeError):
            square = Square(1, 2, "3")

    def test_square_with_negative_width(self):
        with self.assertRaises(ValueError):
            square = Square(-1)

    def test_square_with_negative_height(self):
        with self.assertRaises(ValueError):
            square = Square(1, -2)

    def test_square_with_negative_x(self):
        with self.assertRaises(ValueError):
            square = Square(1, 2, -3)

    def test_square_with_width_and_height_zero(self):
        with self.assertRaises(ValueError):
            square = Square(0)

    def test_square_with_size_and_x(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_square_with_size_x_and_y(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_saving_to_file_None(self):
        """Testing saving a file into json format sending None"""
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual("[]", content)


if __name__ == '__main__':
    unittest.main()
