
import unittest
import sys
import os

sys.path.append(os.path.abspath("../back_end"))
from back_end.app import calculate

class MyTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("2+3"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate("5-3"), 2)

    def test_multiplication(self):
        self.assertEqual(calculate("5*3"), 15)

    def test_division(self):
        self.assertEqual(calculate("9/3"), 3)

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculate("5/0"))

    def test_Empty(self):
        with self.assertRaises(ValueError) as ctx:
            calculate("")

        self.assertEqual(str(ctx.exception), "empty expression")

    def test_multiple_operators(self):
        with self.assertRaises(ValueError) as ctx:
            calculate("2++3")

        self.assertEqual(str(ctx.exception), "only one operator is allowed")

    def test_invalid_format(self):
        with self.assertRaises(ValueError) as ctx:
            calculate("52+")

        self.assertEqual(str(ctx.exception), "invalid expression format")
    def test_not_a_number(self):
        with self.assertRaises(ValueError) as ctx:
            calculate("a+b")

        self.assertEqual(str(ctx.exception), "operands must be numbers")





if __name__ == '__main__':
    unittest.main()

