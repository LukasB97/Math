import unittest
from random import randint

from src.Calculus.Interpolation.InterpolationAlgorithm import InterpolationAlgorithm
from src.Calculus.Interpolation.LagrangeInterpolation import LagrangeInterpolation
from src.Calculus.Interpolation.NewtonInterpolation import NewtonInterpolation

d_1 = [(0, 1), (1, 2), (2, 0), (3, 1)]
d_2 = [(1, 1), (3, 23), (4, 13), (5, 5)]

dataset = [d_2, d_1]


class InterpolationTests(unittest.TestCase):

    @staticmethod
    def create_data_points(size=10, variables=None):
        if variables is None:
            variables = ["x"]
        data_points = []
        for i in range(size):
            fun_input = dict()
            fun_output = dict()
            for var in variables:
                fun_input[var] = randint(-100, 100)
                fun_output[var] = randint(-100, 100)
            data_points.append((fun_input, fun_output))
        return data_points

    def algorithm_test(self, algorithm: InterpolationAlgorithm, variables=None, iterations=20, delta=0):
        for i in range(iterations):
            data_points = self.create_data_points(variables=variables)
            interpolated_function = algorithm.create_polynomial(data_points)
            for data_point in data_points:
                interpolated_result = interpolated_function(**data_point[0])
                self.assertEqual(data_point[1], interpolated_result)

    def test_lagrange(self):
        self.algorithm_test(LagrangeInterpolation())

    def test_newton(self):
        self.algorithm_test(NewtonInterpolation())


if __name__ == '__main__':
    unittest.main()
