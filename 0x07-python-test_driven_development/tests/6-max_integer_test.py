#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A test class for MaxInteger."""
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_MaxInteger(self):
        """Possible test cases."""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([15, 10, 5, -5, -10, 15]), 15)
        self.assertEqual(max_integer([15, 15, 15]), 15)

    def test_typeerror(self):
        """Test handle type errors."""
        self.assertRaises(TypeError, max_integer, ["h", 2])
        self.assertRaises(TypeError, max_integer, [2, [3, 4]])
