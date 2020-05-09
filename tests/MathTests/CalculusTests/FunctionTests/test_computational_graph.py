import parser as std_parser
import unittest
from random import randint

from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser


class ComputationalGraphTests(unittest.TestCase):

    def result_test(self, parser, expression, iterations=10):
        code = std_parser.expr(expression).compile()
        graph = parser.parse(expression)
        parameter = dict()
        for i in range(iterations):
            for variable in graph.get_variable_context():
                parameter[variable] = randint(0, 100)
            self.assertEqual(eval(code, parameter), graph(**parameter))
        eval(code)

    def test_linear_function(self):
        parser = FunctionParser()
        self.result_test(parser, "x")
        self.result_test(parser, "2x-5")
        self.result_test(parser, "(-1.36)*x+4")

    def test_get_bracket_section(self):
        input_data = list("a((c+3*5)*3)")
        result = list("c+3*5")
        self.assertEqual(FunctionParser.get_bracket_section(input_data, 2), result)

    def test_parse(self, x=2.1, a=4, y=3.4):
        parser = FunctionParser()
        graph = parser.parse("x y* a+ (5*2)")
        result = graph.evaluate(x=x, y=y, a=a)
        self.assertEqual(result, x * y * a + (5 * 2))
        graph = parser.parse("x^2+5")
        result = graph.evaluate(x=x)
        self.assertEqual(result, x ** 2 + 5)
        graph = parser.parse("x^x*3")
        result = graph.evaluate(x=x)
        self.assertEqual(result, x ** x * 3)
        graph = parser.parse("a^(14*x)+13*2-1")
        result = graph.evaluate(x=x, a=a)
        self.assertEqual(result, a ** (14 * x) + 13 * 2 - 1)
        graph = parser.parse("(x+2)13*x^2")
        result = graph.evaluate(x=x)
        self.assertEqual(result, (x + 2) * 13 * x ** 2)
        graph = parser.parse("(x^3*4+(4/y*(13+2)))*5")
        result = graph.evaluate(x=x, y=y)
        self.assertEqual(result, (x ** 3 * 4 + (4 / y * (13 + 2))) * 5)


if __name__ == '__main__':
    unittest.main()
