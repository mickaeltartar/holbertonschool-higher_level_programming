#!/usr/bin/python3
""" Unittest for Base class """

import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Testing instantiation of Base class """

    def test_no_instance_creation(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_instance_creation_with_id(self):
        base1 = Base(10)
        self.assertEqual(base1.id, 10)

    def test_more_creation(self):
        base1 = Base(11)
        base2 = Base(42)
        base3 = Base(1337)
        self.assertEqual(base1.id, 11)
        self.assertEqual(base2.id, 42)
        self.assertEqual(base3.id, 1337)

    def test_None_id(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_negative_id(self):
        self.assertEqual(-5, Base(-5).id)

    def test_float_id(self):
        self.assertEqual(3.14, Base(3.14).id)

    def test_zero_id(self):
        self.assertEqual(0, Base(0).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    # JSON
    def test_empty_list(self):
        """ Testing with empyt list """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_non_empty_list(self):
        """ Testing with non-empty list"""
        list_of_dicts = [
            {"key1": "val1", "key2": "val2"}, {"key3": "val3"}]
        result = Base.to_json_string(list_of_dicts)
        expected_json = '[{"key1": "val1", "key2": "val2"}, {"key3": "val3"}]'
        self.assertEqual(result, expected_json)

    def test_none_list(self):
        """ Test with None list """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_non_empty_dict(self):
        """ Test with non-empty dict """
        dict_of_dicts = {"key1": "value1", "key2": "value2"}
        result = Base.to_json_string(dict_of_dicts)
        expected_json = '{"key1": "value1", "key2": "value2"}'
        self.assertEqual(result, expected_json)

    def test_non_empty_string(self):
        """ Test with non-empty string """
        string_of_dicts = "key1:value1,key2:value2"
        result = Base.to_json_string(string_of_dicts)
        expected_json = '"key1:value1,key2:value2"'
        self.assertEqual(result, expected_json)

    def test_list_of_dicts(self):
        """ Test with non-empty list of dicts """
        list_of_dicts = [
            {"key1": "val1", "key2": "val2"}, {"key3": "val3"}]
        result = Base.to_json_string(list_of_dicts)
        expected_json = '[{"key1": "val1", "key2": "val2"}, {"key3": "val3"}]'
        self.assertEqual(result, expected_json)

    def test_list_of_strings(self):
        """ Test with list of strings """
        list_of_strings = ["key1:value1", "key2:value2"]
        result = Base.to_json_string(list_of_strings)
        expected_json = '["key1:value1", "key2:value2"]'
        self.assertEqual(result, expected_json)

    def test_list_of_ints(self):
        """ Test with non-empty list of ints """
        list_of_ints = [1, 2, 3]
        result = Base.to_json_string(list_of_ints)
        expected_json = '[1, 2, 3]'
        self.assertEqual(result, expected_json)

    def test_list_of_floats(self):
        """ Test with non-empty list of floats """
        list_of_floats = [1.1, 2.2, 3.3]
        result = Base.to_json_string(list_of_floats)
        expected_json = '[1.1, 2.2, 3.3]'
        self.assertEqual(result, expected_json)

    # SAVE TO FILE
    def test_save_rectangle_to_file(self):
        """ Test save rectangle to file """
        rect1 = Rectangle(4, 3)
        rect2 = Rectangle(5, 2)
        rect3 = Rectangle(7, 1)
        rectangles = [rect1, rect2, rect3]
        Rectangle.save_to_file(rectangles)
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertTrue(data)

    def test_save_square_to_file(self):
        """ Test save square to file """
        square1 = Square(4)
        square2 = Square(5)
        square3 = Square(7)
        squares = [square1, square2, square3]
        Square.save_to_file(squares)
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertTrue(data)

    def test_save_to_file_none(self):
        """ Test save to file with None """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_empty(self):
        """ Test save to file with empty list """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_empty_dict(self):
        """ Test save to file with empty dict """
        Square.save_to_file({})
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_empty_string(self):
        """ Test save to file with empty string """
        Square.save_to_file("")
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_empty_tuple(self):
        """ Test save to file with empty tuple """
        Square.save_to_file(())
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_empty_set(self):
        """ Test save to file with empty set """
        Square.save_to_file(set())
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    def test_save_to_file_empty_list(self):
        """ Test save to file with empty list """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

    # FROM JSON STRING
    def test_from_json_string_valid(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]'
        result = Base.from_json_string(json_string)
        self.assertIsInstance(result, list)
        self.assertEqual(result, [{"id": 1, "name": "John"}, {
                         "id": 2, "name": "Alice"}])

    def test_from_json_empty(self):
        """ Test from json with empty string """
        json_string = ''
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_none(self):
        """ Test from json with None """
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    # CREATE
    def test_create_rectangle(self):
        """ Test create rectangle  """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle_instance, Rectangle)

    def test_create_square(self):
        """ Test create square  """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertIsInstance(square_instance, Square)

    def test_create_rectangle_with_id(self):
        """ Test create rectangle with id """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.id, 1)

    def test_create_square_with_id(self):
        """ Test create square with id """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.id, 1)

    def test_create_rectangle_with_x(self):
        """ Test create rectangle with x """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.x, 2)

    def test_create_square_with_x(self):
        """ Test create square with x """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.x, 2)

    def test_create_rectangle_with_y(self):
        """ Test create rectangle with y """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.y, 3)

    def test_create_square_with_y(self):
        """ Test create square with y """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.y, 3)

    def test_create_rectangle_with_width(self):
        """ Test create rectangle with width """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.width, 5)

    def test_create_square_with_width(self):
        """ Test create square with width """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.size, 5)

    def test_create_rectangle_with_height(self):
        """ Test create rectangle with height """
        rectangle_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.height, 10)

    def test_create_square_with_height(self):
        """ Test create square with height """
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.id, 1)

    # DICTIONARY
    def test_rectangle_to_dictionary(self):
        """ Testing to_dictionary method of Rectangle """
        rectangle = Rectangle(5, 2, 3, 0, id=1)
        dictionary = rectangle.to_dictionary()
        expected_dict = {
            "id": 1,
            "width": 5,
            "height": 2,
            "x": 3,
            "y": 0
        }
        self.assertEqual(dictionary, expected_dict)
        self.assertIsInstance(dictionary, dict)

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

    # LOAD FROM FILE
    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_empty_file(self):
        with open("Square.json", "w") as file:
            file.write("")
        output = Square.load_from_file()
        self.assertEqual([], output)
        os.remove("Square.json")
        file.close()
        self.assertFalse(os.path.exists("Square.json"))

    def test_load_rectangle(self):
        """ Test load rectangle """
        rectangle1 = Rectangle(2, 4)
        rectangle2 = Rectangle(4, 8)
        Rectangle.save_to_file([rectangle1, rectangle2])
        rectangle_output = Rectangle.load_from_file()
        self.assertEqual(str(rectangle1), str(rectangle_output[0]))
        self.assertEqual(str(rectangle2), str(rectangle_output[1]))

    def test_load_square(self):
        """ Test load square """
        square1 = Square(2)
        square2 = Square(4)
        Square.save_to_file([square1, square2])
        square_output = Square.load_from_file()
        self.assertEqual(str(square1), str(square_output[0]))
        self.assertEqual(str(square2), str(square_output[1]))


if __name__ == '__main__':
    unittest.main()
