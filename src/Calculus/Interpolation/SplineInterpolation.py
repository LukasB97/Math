from typing import Set, Tuple, List

from src.Algebra.Structures.Function.Function import Function
from src.Calculus.Interpolation import InterpolationAlgorithm


class SplineInterpolation(InterpolationAlgorithm):

    def __init__(self, k):
        self.k = k

    def first_derivative(self, b, c, d, x_j, x):
        return b + 2 * c *(x - x_j) + 3 * d * (x - x_j) ** 2

    def second_derivative(self, c, d, x_j, x):
        return 2 * c + 6 * d * (x - x_j)

    def base_function(self, a, b, c, d, x_j, x):
        return a + b * (x - x_j) + c * (x - x_j) ** 2 + d * (x - x_j) ** 3

    def create_first_derivative_condition(self, next_b, next_c, next_d, next_x, x):
        return [0, 1, 0, 0], self.first_derivative(next_b, next_c, next_d, next_x, x)

    def create_second_derivative_condition(self, next_c, next_d, next_x, x):
        return [0, 0, 2, 0], self.second_derivative(next_c, next_d, next_x, x)

    def create_base_condition(self, x, next_x, y):
        return [1, next_x - x, (next_x - x) ** 2, (next_x - x) ** 3], self.base_function()


    def get_coefficients(self, x, a, b, c, d, next_x, next_y):
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
        first_der_cond, first_solution = self.create_first_derivative_condition(b, c, d, next_x, x)
        second_der_cond, second_solution = self.create_second_derivative_condition(c, d, next_x, x)
        a = [
            [1, 0, 0, 0],  # Sj(xj) = f(xj)
            second_der_cond,
            first_der_cond,
            second_der_cond
        ]
        pass


    def create_polynomial(self, data_points: Set[Tuple]) -> Function:
        pass
