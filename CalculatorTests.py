import unittest

from Calculator import Calculator
from CsvReader import CsvReader


class CalTestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiated_calculator(self):
        calculator: Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def test_subtraction(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_addition(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.mul(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.div(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqr(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareRoot(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.sqrt(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    if __name__ == '__main__':
        unittest.main()
