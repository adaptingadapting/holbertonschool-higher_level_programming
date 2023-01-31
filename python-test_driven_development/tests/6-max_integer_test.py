#!/usr/bin/python3

""" test module for the max integer function """


import unittest
max_integer = __import__("6-max_integer").max_integer


class test_function_valid(unittest.TestCase):
    """ class for testing edge cases """

    def test_empty_list(self):
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_no_arg_passed(self):
        self.assertIsNone(max_integer())

    def test_one_arg(self):
        new_list = [1]
        self.assertEqual(max_integer(new_list), 1)

    def test_wrong_type(self):
        self.assertRaises(TypeError, max_integer, None)
        max_integer("hola")
        new_list = ["hola", 2]
        self.assertRaises(TypeError, max_integer, new_list)

    def test_values(self):
        new_list = [-1, -2, -3]
        self.assertEqual(max_integer(new_list), -1)
        new_list = [1, -1]
        self.assertEqual(max_integer(new_list), 1)

    def test_posiiton(self):
        new_list = [23, 45, 12]
        self.assertEqual(max_integer(new_list), 45)
        new_list = [45, 23, 12]
        self.assertEqual(max_integer(new_list), 45)
        new_list = [12, 23, 45]
        self.assertEqual(max_integer(new_list), 45)
