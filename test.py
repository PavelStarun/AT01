import unittest
from main import add, subtract, multiply, divide, mod_division

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-5, -5), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-10, -2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)
    def test_mod_division(self):
        self.assertEqual(mod_division(10, 3), 1)
        self.assertEqual(mod_division(10, 2), 0)
        self.assertEqual(mod_division(-10, 3), 2)
        self.assertEqual(mod_division(10, -3), -2)
        self.assertEqual(mod_division(-10, -3), -1)

        with self.assertRaises(ValueError): mod_division(10, 0)


if __name__ == "__main__":
    unittest.main()
