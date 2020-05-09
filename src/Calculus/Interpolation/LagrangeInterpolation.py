from typing import Tuple, List

from src.Algebra.Structures.Function.Parser.FunctionParser import FunctionParser
from src.Algebra.Structures.Function.Polynomial.Polynomial import Polynomial
from src.Calculus.Interpolation.InterpolationAlgorithm import InterpolationAlgorithm


class LagrangeInterpolation(InterpolationAlgorithm):

    def create_polynomial(self, data_points: List[Tuple]) -> Polynomial:
        polynomial = data_points[0][1] * self.create_base(data_points, 0)
        for i in range(1, len(data_points)):
            polynomial += data_points[i][1] * self.create_base(data_points, i)
        return polynomial

    @staticmethod
    def create_base(data_points: List[Tuple], j):
        parser = FunctionParser()
        base = parser.parse("1*1")
        for i in range(len(data_points)):
            if i == j:
                continue
            fun_str = "(x-" + str(data_points[i][0]) + ")"
            fun_str += "/" + str(data_points[j][0] - data_points[i][0])
            base *= parser.parse(fun_str)
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

    def rec(self, data_points: List):
        print(data_points)
        if len(data_points) == 1:
            return data_points[0]
        if len(data_points) == 2:
            return data_points[1][1] - data_points[0][1]
        first = []
        second = []
        for i in range(len(data_points)):
            if i > 0:
                first.append(data_points[i])
            if i < len(data_points) - 1:
                second.append(data_points[i])
        coeff = 1 / data_points[-1][0] - data_points[0][0]
        return coeff * (self.rec(first) - self.rec(second))
