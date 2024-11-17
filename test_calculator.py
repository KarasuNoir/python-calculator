import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Add test cases for `add`
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    # Add test cases for `subtract`
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    # Add test cases for `multiply`
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    # Add test cases for `divide`
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    # Add test cases for `modulo`
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)


if __name__ == "__main__":
    unittest.main()