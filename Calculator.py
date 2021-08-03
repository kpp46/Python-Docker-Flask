from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Divide import Division
from Square import Square
from SquareRoot import SquareRoot

from CsvReader import CsvReader


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        addition = Addition(self, a, b)
        self.result = addition.result

    def sub(self, a, b):
        subtract = Subtraction(self, a, b)
        self.result = subtract.result

    def mul(self, a, b):
        multi = Multiplication(self, a, b)
        self.result = multi.result

    def div(self, a, b):
        divide = Division(self, a, b)
        self.result = divide.result

    def sqr(self, a):
        square = Square(self, a)
        self.result = square.result

    def sqrt(self, a):
        squareroot = SquareRoot(self, a)
        self.result = squareroot.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass
