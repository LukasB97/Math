import math
import parser as std_parser
import unittest
from random import randint

from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import Mul, Pow, Div, Sub, Add
from src.Algebra.Structures.Function.Variable import Variable


class ComputationalGraphTests(unittest.TestCase):

    def result_test(self, graph, expression, iterations=10):
        code = std_parser.expr(expression).compile()
        parameter = dict()
        for i in range(iterations):
            for variable in graph.get_variable_context():
                parameter[variable] = randint(0, 100)
            self.assertEqual(eval(code, parameter), graph(**parameter))
        eval(code)

    def test_mul(self):
        mul = Mul(1, 2)
        self.assertEqual(mul(), math.factorial(2))
        mul.add_operand(3)
        self.assertEqual(mul(), math.factorial(3))
        mul *= 4
        self.assertEqual(mul(), math.factorial(4))

    def test_div(self):
        div = Div(math.factorial(5), 5)
        self.assertEqual(div(), math.factorial(4))
        div /= 4
        self.assertEqual(div(), math.factorial(3))
        div /= 3
        self.assertEqual(div(), math.factorial(2))
        with self.assertRaises(NotImplementedError):
            div.add_operand(2)

    def test_add(self):
        add = Add(1, 2)
        self.assertEqual(add(), 3)
        add.add_operand(4)
        self.assertEqual(add(), 7)
        add += 5
        self.assertEqual(add(), 12)

    def test_sub(self):
        sub = Sub(12, 2)
        self.assertEqual(sub(), 10)
        sub.add_operand(3)
        self.assertEqual(sub(), 7)
        sub -= 4
        self.assertEqual(sub(), 3)

    def test_pow(self):
        pow = Pow(2, 1)
        self.assertEqual(pow(), 2)
        pow **= 2
        self.assertEqual(pow(), 4)
        pow **= 2
        self.assertEqual(pow(), 16)
        with self.assertRaises(NotImplementedError):
            pow.add_operand(2)

    def test_fuzz(self):
        operation = Add(3, 1)
        self.assertEqual(4, operation())
        operation **= 2
        self.assertEqual(16, operation())
        operation -= 3
        self.assertEqual(13, operation())
        operation *= 4
        self.assertEqual(52, operation())
        operation.add_operand(3)
        self.assertEqual(156, operation())
        operation /= 156
        self.assertEqual(1, operation())
        operation += 15
        self.assertEqual(16, operation())

    def test_fuzz_2(self):
        operation = Add(3, Variable("x"))
        self.assertEqual(5, operation(2))
        operation **= 2
        self.assertEqual(10, operation())
        operation -= Variable("x")
        self.assertEqual(13, operation())
        operation *= 4
        self.assertEqual(52, operation())
        operation.add_operand(3)
        self.assertEqual(156, operation())
        operation /= 156
        self.assertEqual(1, operation())
        operation += 15
        self.assertEqual(16, operation())


if __name__ == '__main__':
    unittest.main()
