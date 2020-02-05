import math

from src.Algebra.Structures.Function.Evaluable import Evaluable
from src.Algebra.Structures.Function.Function import Function
from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from src.Algebra.Structures.Polynomial import Polynomial


class TaylorPolynomial(Polynomial):

    def upper_error_bound(self, x):
        pass

    @classmethod
    def build_order(cls, derivative_of_order: Evaluable, approximation_point: float, order: int):
        coefficient = derivative_of_order.evaluate(approximation_point) / math.factorial(order)
        if order == 0:
            return coefficient
        return coefficient * FunctionParser.parse_string("(x-" + str(approximation_point) + ")^" + str(order))

    def __init__(self, fun_to_approximate: Function, approximation_point: float, order: int):
        super().__init__()
        self.order = order
        self.approximation_point = approximation_point
        polynomial = Polynomial()
        assert len(fun_to_approximate.get_variable_context()) == 1
        for i in range(order):
            polynomial += self.build_order(fun_to_approximate, approximation_point, i)
            fun_to_approximate = fun_to_approximate.get_derivative("x")
