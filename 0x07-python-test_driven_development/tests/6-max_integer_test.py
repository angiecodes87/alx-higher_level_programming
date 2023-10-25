"""
Unit test for max_integer function.
"""

import unittest
from your_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([4, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([8, 234, 332, 33]), 332)
        self.assertAlmostEqual(max_integer([-1, -2, -3]), -1)
        self.assertAlmostEqual(max_integer([20000000022]), 20000000022)
        self.assertAlmostEqual(max_integer([]), None)

    def test_non_integer_input(self):
        self.assertRaises(TypeError, max_integer, True)

