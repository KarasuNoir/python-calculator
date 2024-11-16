import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Add
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)

    # Subtract
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 5), -2)

    # Multiply
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 7), 0)

    # Divide
    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_remainder(self):
        self.assertEqual(self.calc.divide(11, 2), 5)

    # Modulo
    def test_modulo_exact(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

    def test_modulo_non_exact(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)