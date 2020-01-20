from typing import Tuple, List

from src.Algebra.Structures.Function import FunctionParser
from src.Algebra.Structures.Function.Function import Function
from src.Calculus.Interpolation import InterpolationAlgorithm


class LagrangeInterpolation(InterpolationAlgorithm):

    def create_polynomial(self, data_points: List[Tuple]) -> Function:
        polynomial = data_points[0][1] * self.create_base(data_points, 0)
        for i in range(1, len(data_points)):
            polynomial += data_points[i][1] * self.create_base(data_points, i)
        return polynomial

    def create_base(self, data_points: List[Tuple], j):
        base = FunctionParser.parse_string("1*1")
        for i in range(len(data_points)):
            if i == j:
                continue
            fun_str = "(x-" + str(data_points[i][0]) + ")"
            fun_str += "/" + str(data_points[j][0] - data_points[i][0])
            base *= FunctionParser.parse_string(fun_str)
        return base

    def divided_differences(self, data_points: List[Tuple], i):
        if i == 0:
            return data_points[0][1]
        e = data_points[:i + 1]
        print("diff of ", e, " is: ")
        res = self.rec(e)
        print(
            res
        )
        return res

    def rec(self, l: List):
        print(l)
        if len(l) == 1:
            return l[0]
        if len(l) == 2:
            return l[1][1] - l[0][1]
        first = []
        second = []
        for i in range(len(l)):
            if i > 0:
                first.append(l[i])
            if i < len(l) - 1:
                second.append(l[i])
        coeff = 1 / l[-1][0] - l[0][0]
        return coeff * (self.rec(first) - self.rec(second))