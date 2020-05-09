import unittest

from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from src.Calculus.FixedPointIteration import NewtonsMethod


class FixedPointIterationTests(unittest.TestCase):

    def test_linear_function(self):
        parser = FunctionParser()
        graph = parser.parse("10-x^2")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r1 = newton.iterate(1, 30)
        print("x=", r1, " f(x)=", graph.evaluate(r1))
        graph = parser.parse("1+0.009*x^3")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r2 = newton.iterate(1, 30)
        print("x=", r2, " f(x)=", graph.evaluate(r2))
        self.assertEqual("1", "")

    def test_lf(self):
        parser = FunctionParser()
        graph = parser.parse("x^3-10")
        newton = NewtonsMethod.NewtonsMethod(graph)
        r2 = newton.iterate(100, 300)
        print("x=", r2, " f(x)=", graph.evaluate(r2))
        self.assertEqual("1", "")

    def test_der(self):
        parser = FunctionParser()
        graph = parser.parse("3x^2-x-0.5")
        newton = NewtonsMethod.NewtonsMethod(graph)
        self.assertEqual("1", "")


if __name__ == '__main__':
    unittest.main()
