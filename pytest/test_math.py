import unittest
from math_operations import math_add, subtract, multiply, divide

class TestMathFunctions(unittest.TestCase):

    def test_math_add(self):
        self.assertEqual(math_add(3, 4), 7)
        self.assertEqual(math_add(-1, 1), 0)
        self.assertEqual(math_add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), 5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(9, 3), 3)
        self.assertEqual(divide(7, 2), 3)  # Integer division

if __name__ == '__main__':
    unittest.main()
