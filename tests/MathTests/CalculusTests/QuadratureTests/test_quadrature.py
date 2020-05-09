import unittest

from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from src.Calculus.Integration.QuadratureAlgorithm import QuadratureAlgorithm


class QuadratureTest(unittest.TestCase):

    @staticmethod
    def test_simple_derivative():
        parser = FunctionParser()
        q = QuadratureAlgorithm(3)
        graph = parser.parse("x^2+5")
        q.approximate_integral(graph, 1, 2)


if __name__ == '__main__':
    unittest.main()
