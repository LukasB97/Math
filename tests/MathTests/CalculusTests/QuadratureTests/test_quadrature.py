import parser
import unittest
from time import time

from Calculus.Integration.QuadratureAlgorithm import QuadratureAlgorithm
from src.Algebra.Structures.Function.Operation import ComputationalGraphPart
from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from tests.MathTests.CalculusTests.FunctionTests import Functions


class QuadratureTest(unittest.TestCase):


    def test_simple_derivative(self):
        q = QuadratureAlgorithm(3)
        graph = FunctionParser.parse_string("x^2+5")
        q.approximate_integral(graph)


if __name__ == '__main__':
    unittest.main()
