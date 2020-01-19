from typing import Set, Tuple, List

from src.Algebra.Structures.Function.Function import Function
from src.Calculus.Interpolation import InterpolationAlgorithm


class SplineInterpolation(InterpolationAlgorithm):

    def __init__(self, k):
        self.k = k


    def lee(self, data_points: List[Tuple], i):
        """
        Sj(x)= aj + bj * (x−xj)+ cj * (x−xj)^2 + dj * (x−xj)^3 für xj<=x<=xj+1
        Sj(xj) = f(xj)
        Sj(x(j+1)) = f(x(j+1))
        S'j(xj) = S'j+1(xj)
        S''j(xj) = S''j+1(xj)
        S'j(x) = bj + 2cj * (x-xj) + 3dj * (x-xj)^2
        S''j(x) = 2cj + 6dj * (x-xj)
        S''(a) = S''(b) = 0
        :return:
        """
        x_i = data_points[i][0]
        y_i = data_points[i][1][0]
        next_x_i = data_points[i+1][0]
        next_y_i = data_points[i+1][1][0]
        pass


    def create_polynomial(self, data_points: Set[Tuple]) -> Function:
        pass
