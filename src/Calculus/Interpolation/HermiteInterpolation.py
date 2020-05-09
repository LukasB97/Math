from typing import Tuple, List

from src.Algebra.Structures.Function.Polynomial.Polynomial import Polynomial
from src.Calculus.Interpolation import InterpolationAlgorithm


class HermiteInterpolation(InterpolationAlgorithm):

    def create_polynomial(self, data_points: List[Tuple]) -> Polynomial:
        basis = []
        for i in range(len(data_points)):
            basis.append(self.create_base(data_points, i))
        coeffs = []
        for i in range(len(data_points)):
            coeffs.append(self.divided_differences(data_points, i))
        return Polynomial(coeffs)

    @staticmethod
    def create_base(data_points: List[Tuple], degree):
        raise NotImplementedError()
        # base = FunctionParser.parse_string("1*1")
        # for i in range(degree - 1):
        #     fun_str = "x-" + str(data_points[i][0])
        #     base * FunctionParser.parse_string(fun_str)
        # return base

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
            coeff = 1 / (data_points[-1][0] - data_points[0][0])
            return coeff * (data_points[1][1] - data_points[0][1])
        first = []
        second = []
        for i in range(len(data_points)):
            if i > 0:
                first.append(data_points[i])
            if i < len(data_points) - 1:
                second.append(data_points[i])
        coeff = 1 / (data_points[-1][0] - data_points[0][0])
        return coeff * (self.rec(first) - self.rec(second))
