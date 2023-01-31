#!/usr/bin/python3

""" test module for the max integer function """


import unittest
max_integer = __import__("6-max_integer").max_integer


class test_function_valid(unittest.TestCase):
    """ class for testing edge cases """

    def test_empty_list(self):
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_no_arg_passed(self):
        self.assertEqual(max_integer(), None)

    def test_one_arg(self):
        new_list = [1]
        self.assertEqual(max_integer(new_list), 1)

    def test_wrong_type(self):
        new_list = "string"
        self.assertRaises(TypeError, max_integer, new_list)
        self.assertRaises(TypeError, max_integer, {"hola": 2})
        self.assertRaises(TypeError, max_integer, (0, 0))
        self.assertRaises(TypeError, max_integer, 2.4)
        self.assertRaises(TypeError, max_integer, [2, 3])
        self.assertRaises(TypeError, max_integer, None)
