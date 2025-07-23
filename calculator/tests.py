import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_expression(self):
        result = self.calculator.evaluate("3 + 7 * 2")
        self.assertEqual(result, 17)

if __name__ == "__main__":
    unittest.main()