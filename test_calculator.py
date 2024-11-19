import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(6, 10), 16)

    def test_add2(self):
        self.assertEqual(self.calc.add(-6, 8), 2)
        self.assertEqual(self.calc.add(6, -10), -6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1, 2), 1)
        self.assertEqual(self.calc.subtract(6, 11), 5)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-6, 11), 17)
        self.assertEqual(self.calc.subtract(6, -11), -17)
        self.assertEqual(self.calc.subtract(-6, -11), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-1, 20), -20)
        self.assertEqual(self.calc.multiply(20, -1), -20)
        self.assertEqual(self.calc.multiply(-20, -1), 20)


    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(12, -2), -6)
        self.assertEqual(self.calc.divide(-12, 2), -6)
        self.assertEqual(self.calc.divide(-12, -2), 6)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(7, 0), "No answer")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(-7, 3), 2)
        self.assertEqual(self.calc.modulo(-22, 7), 6)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(22, -7), 6)
        self.assertEqual(self.calc.modulo(-22, -7), 6)
        self.assertEqual(self.calc.modulo(-50, -8), 6)

if __name__ == '__main__':
    unittest.main()