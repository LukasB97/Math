import parser
import unittest
from time import time

from src.AlgebraicStructures.Function.FunctionParser import FunctionParser
from src.AlgebraicStructures.Function.Operator1 import Operator
from src.Calculus.FixedPointIteration import NewtonsMethod


class FixedPointIterationTests(unittest.TestCase):

    def test_linear_function(self, x=2.1, a=4, y=3.4):
        graph = FunctionParser.parse_string("10+x^2")
        r1 = NewtonsMethod.start(graph, 1, 30)
        print("x=", r1, " f(x)=", graph.evaluate(x=r1))
        graph = FunctionParser.parse_string("1+0.009*x^3")
        r2 = NewtonsMethod.start(graph, 1, 30)
        print("x=", r2, " f(x)=", graph.evaluate(x=r2))




if __name__ == '__main__':
    unittest.main()
