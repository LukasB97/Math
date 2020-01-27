import unittest

from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from src.Calculus.FixedPointIteration import NewtonsMethod


class FixedPointIterationTests(unittest.TestCase):

    def test_fixed_point_iteration(self, s):
        pass

    def test_linear_function(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("10-x^2")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r1 = newton.iterate(1, 30)
        print("x=", r1, " f(x)=", graph.evaluate(r1))
        graph = FunctionParser.parse_string("1+0.009*x^3")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r2 = newton.iterate(1, 30)
        print("x=", r2, " f(x)=", graph.evaluate(r2))

    def test_lf(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("x^3-10")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r2 = newton.iterate(100, 300)
        print("x=", r2, " f(x)=", graph.evaluate(r2))

    def test_der(self):
        graph = FunctionParser.parse_string("3x^2-x-0.5")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r2 = newton.iterate(100, 300)


if __name__ == '__main__':
    unittest.main()
