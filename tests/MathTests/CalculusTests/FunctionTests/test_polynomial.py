import parser as std_parser
import random
import unittest
from random import randint

from src.Algebra.Structures.Function.Polynomial.Polynomial import Polynomial


class PolynomialTest(unittest.TestCase):

    def result_test(self, graph, expression, iterations=10):
        code = std_parser.expr(expression).compile()
        parameter = dict()
        for i in range(iterations):
            for variable in graph.get_variable_context():
                parameter[variable] = randint(0, 100)
            self.assertEqual(eval(code, parameter), graph(**parameter))
        eval(code)

    def test_evaluation(self):
        p = Polynomial([1, 1, 2, -3])
        self.assertEqual(p(0), 1)
        self.assertEqual(p(1), 1)
        self.assertEqual(p(3), -59)

    def test_mul(self):
        p1 = Polynomial([1, 1, 2, -3])
        p2 = Polynomial([5, 1, 2, -3, 3, 2])
        self._test_mul(p1, p2, 5)
        p1 *= Polynomial([-1])
        self._test_mul(p1, p2)
        self._test_mul(p1 * p2, p2)

    def _test_mul(self, p1, p2, iterations=10):
        p = p1 * p2
        for i in range(iterations):
            x = random.randint(-100, 100)
            self.assertEqual(p(x), p1(x) * p2(x))

    def test_add(self):
        p1 = Polynomial([1, 1, 2, -3])
        p2 = Polynomial([5, 1, 2, -3, 3, 2])
        self._test_add(p1, p2, 5)
        p1 += Polynomial([-1])
        self._test_add(p1, p2)
        self._test_add(p1 + p2, p2)

    def _test_add(self, p1, p2, iterations=10):
        p = p1 + p2
        for i in range(iterations):
            x = random.randint(-100, 100)
            self.assertEqual(p(x), p1(x) + p2(x))

    def test_div(self):
        p1 = Polynomial([1, 1, 2, -3])
        p2 = Polynomial([5, 1, 2, -3, 3, 2])
        self._test_div(p1, p2, 5)
        p1 /= Polynomial([-1])
        self._test_div(p1, p2)
        self._test_div(p1 / p2, p2)

    def _test_div(self, p1, p2, iterations=10):
        p = p1 / p2
        for i in range(iterations):
            x = random.randint(-100, 100)
            self.assertEqual(p(x), p1(x) / p2(x))

    def test_sub(self):
        p1 = Polynomial([1, 1, 2, -3])
        p2 = Polynomial([5, 1, 2, -3, 3, 2])
        self._test_sub(p1, p2, 5)
        p1 -= Polynomial([-1])
        self._test_sub(p1, p2)
        self._test_sub(p1 - p2, p2)

    def _test_sub(self, p1, p2, iterations=10):
        p = p1 - p2
        for i in range(iterations):
            x = random.randint(-100, 100)
            self.assertEqual(p(x), p1(x) - p2(x))

    def test_fuzz(self):
        pass

    def test_fuzz_2(self):
        pass


if __name__ == '__main__':
    unittest.main()
