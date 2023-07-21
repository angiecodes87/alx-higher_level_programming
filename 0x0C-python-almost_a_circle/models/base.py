#!/usr/bin/python3
"""Defines unittests for base.py. """

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_instantiation(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)




def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBase))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
