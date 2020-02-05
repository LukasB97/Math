import parser
import unittest
from time import time

from src.Algebra.Structures.Function.Operation import ComputationalGraphPart
from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from tests.MathTests.CalculusTests.FunctionTests import Functions


class ComputationalGraphTests(unittest.TestCase):

    def test_linear_function(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("(x^3*4+(4/y*(13+2)))*5")
        result = graph.evaluate(x=x, y=y)
        self.assertEqual(result, (x ** 3 * 4 + (4 / y * (13 + 2))) * 5)

    def test_get_bracket_section(self):
        input_data = list("a((c+3*5)*3)")
        result = list("c+3*5")
        self.assertEqual(FunctionParser.get_bracket_section(input_data, 2), result)

    def test_build_definition_list(self):
        input_data = "a((c+3*5)*3)"
        result = list(input_data)
        result[4] = ComputationalGraphPart.ADD
        result[6] = ComputationalGraphPart.MUL
        result[9] = ComputationalGraphPart.MUL
        self.assertEqual(FunctionParser.build_definition_list(input_data), result)

    def test_preprocessing(self):
        a = "x y* a+ (5*2)c"
        self.assertEqual(
            FunctionParser.preprocess_string(a),
            "x*y*a+(5*2)*c"
        )

    def test_parse(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("x y* a+ (5*2)")
        result = graph.evaluate(x=x, y=y, a=a)
        self.assertEqual(result, x * y * a + (5 * 2))
        graph = FunctionParser.parse_string("x^2+5")
        result = graph.evaluate(x=x)
        self.assertEqual(result, x ** 2 + 5)
        graph = FunctionParser.parse_string("x^x*3")
        result = graph.evaluate(x=x)
        self.assertEqual(result, x ** x * 3)
        graph = FunctionParser.parse_string("a^(14*x)+13*2-1")
        result = graph.evaluate(x=x, a=a)
        self.assertEqual(result, a ** (14 * x) + 13 * 2 - 1)
        graph = FunctionParser.parse_string("(x+2)13*x^2")
        result = graph.evaluate(x=x)
        self.assertEqual(result, (x + 2) * 13 * x ** 2)
        graph = FunctionParser.parse_string("(x^3*4+(4/y*(13+2)))*5")
        result = graph.evaluate(x=x, y=y)
        self.assertEqual(result, (x ** 3 * 4 + (4 / y * (13 + 2))) * 5)

    def test_performance(self):
        # 13.12.19: std 5x faster
        eq = "(x+2)*13*x**2"
        time1 = time()
        for i in range(100):
            code = parser.expr(eq).compile()
            x = 10
            eval(code)
        time2 = time()
        print(time2 - time1)
        eq = "(x+2)13*x^2"
        time1 = time()
        for i in range(100):
            graph = FunctionParser.parse_string(eq)
            result = graph.evaluate(x=10)
        time2 = time()
        print(time2 - time1)

    def test_profile(self):
        eq = "(x+2)13*x^2"
        for i in range(100):
            graph = FunctionParser.parse_string(eq)
            result = graph.evaluate(x=10)

    def test_simple_derivative(self):
        for fun, derivative in Functions.function_derivative.items():
            fun_graph = FunctionParser.parse_string(fun)
            derivative_graph = FunctionParser.parse_string(derivative)
            self.assertEqual(fun_graph.get_derivative("x"), derivative_graph)


if __name__ == '__main__':
    unittest.main()
