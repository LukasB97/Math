import parser as python_parser
import unittest
from random import randint
from time import time

from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser


class FunctionParserTests(unittest.TestCase):

    def result_test(self, parser, expression, iterations=10):
        code = python_parser.expr(expression).compile()
        function = parser.parse(expression)
        parameter = dict()
        for i in range(iterations):
            for variable in function.get_variable_context():
                parameter[variable] = randint(0, 100)
            self.assertEqual(eval(code, parameter), function(**parameter))

    def concat_test(self, parser, eq1, eq2, sign):
        fun1 = parser.parse(eq1)
        fun2 = parser.parse(eq2)
        if sign == "+":
            fun = fun1 + fun2
        elif sign == "-":
            fun = fun1 - fun2
        elif sign == "*":
            fun = fun1 * fun2
        elif sign == "/":
            fun = fun1 / fun2
        elif sign == "^":
            fun = fun1 ** fun2
        else:
            raise Exception()
        eq = "(" + eq1 + ")" + sign + "(" + eq2 + ")"
        code = python_parser.expr(eq).compile()
        parameter = dict()
        for i in range(10):
            for variable in fun.get_variable_context():
                parameter[variable] = randint(0, 100)
            self.assertEqual(eval(code, parameter), fun(**parameter))

    def test_simple(self):
        parser = FunctionParser()
        self.result_test(parser, "3*18")
        self.result_test(parser, "-2*4+5")
        self.result_test(parser, "1/-10")

    def test_simple_brackets(self):
        parser = FunctionParser()
        self.result_test(parser, "3*(18-7)")
        self.result_test(parser, "-2**(4+5)")
        self.result_test(parser, "1/(-10*2)")
        self.result_test(parser, "(1/-10)*2")

    def test_variable(self):
        parser = FunctionParser()
        self.result_test(parser, "x^2")
        self.result_test(parser, "-2*x+5")
        self.result_test(parser, "x^3+2x^2+0.3x+9")

    def test_variable_brackets(self):
        parser = FunctionParser()
        self.result_test(parser, "x^(2/3)")
        self.result_test(parser, "(-2)*x+5")
        self.result_test(parser, "(x^3+2x)^2+0.3x+9")

    def test_chained_brackets(self):
        parser = FunctionParser()
        self.result_test(parser, "3*(x*(x^2+3))")
        self.result_test(parser, "x/(14*(x^2/x))")
        self.result_test(parser, "(3+6*(1*7+2)/3)")

    def test_concat(self):
        parser = FunctionParser()
        self.concat_test(parser, "3*18", "-2*4+5", "*")
        self.concat_test(parser, "3*(x*(x^2+3))", "-2*x+5", "/")
        self.concat_test(parser, "3*18", "-2**(4+5)", "-")
        self.concat_test(parser, "(-2)*x+5", "(3+6*(1*7+2)/3)", "+")
        self.concat_test(parser, "3*18", "1/-10", "^")
        self.concat_test(parser, "x/(14*(x^2/x))", "-2*4+5", "^")
        self.concat_test(parser, "3*18", "x^3+2x^2+0.3x+9", "*")
        self.concat_test(parser, "x^2", "-2*4+5", "/")
        self.concat_test(parser, "x^3+2x^2+0.3x+9", "(1/-10)*2", "+")

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
