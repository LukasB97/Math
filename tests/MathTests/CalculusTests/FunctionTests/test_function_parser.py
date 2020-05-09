import parser as python_parser
import unittest
from numbers import Number
from time import time

from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import ComputationalGraphPart, Mul
from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from src.Algebra.Structures.Function.Variable import Variable


class FunctionParserTests(unittest.TestCase):

    def check_graph_result(self, graph: ComputationalGraphPart, expected):
        raise NotImplementedError()

    def check_combination(self, parser: FunctionParser, variable, number, input_value):
        variable = parser.parse(variable)
        number = parser.parse(number)
        self.assertIsInstance(variable, Variable)
        self.assertIsInstance(number, Number)
        operation = variable * number
        self.assertIsInstance(operation, Mul)
        self.assertEqual(operation(input_value), input_value * number)

    @staticmethod
    def test_performance():
        # 13.12.19: std 5x faster
        eq = "(x+2)*13*x**2"
        parser = FunctionParser()
        time1 = time()
        for i in range(100):
            code = python_parser.expr(eq).compile()
            eval(code)
        time2 = time()
        print(time2 - time1)
        eq = "(x+2)13*x^2"
        time1 = time()
        for i in range(100):
            graph = parser.parse(eq)
        time2 = time()
        print(time2 - time1)

    @staticmethod
    def test_profile():
        parser = FunctionParser()
        eq = "(x+2)13*x^2"
        for i in range(100):
            graph = parser.parse(eq)


if __name__ == '__main__':
    unittest.main()
