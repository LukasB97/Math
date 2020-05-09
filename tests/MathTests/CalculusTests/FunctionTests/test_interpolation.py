import unittest
from typing import List, Tuple

from src.Calculus.Interpolation.InterpolationAlgorithm import InterpolationAlgorithm
from src.Calculus.Interpolation.NewtonInterpolation import NewtonInterpolation
from src.Calculus.Interpolation.LagrangeInterpolation import LagrangeInterpolation

d_1 = [(0, 1), (1, 2), (2, 0), (3, 1)]
d_2 = [(1, 1), (3, 23), (4, 13), (5, 5)]

dataset = [d_2, d_1]


class FixedPointIterationTests(unittest.TestCase):

    def test_algorithm(self, algorithm: InterpolationAlgorithm, data_points: List[Tuple], delta=0):
        interpolated_function = algorithm.create_polynomial(data_points)
        for data_point in data_points:
            interpolated_result = interpolated_function.evaluate(x=data_point[0])
            self.assertAlmostEqual(data_point[1], interpolated_result, delta=delta)

    def test_lagrange(self):
        interp = LagrangeInterpolation()
        data_points = [
            (0, 1), (1, 2), (2, 0), (3, 1)
        ]
        self.test_algorithm(interp, data_points)

    @staticmethod
    def test_newton():
        interp = NewtonInterpolation()
        data_points = [
            (0, 1), (1, 2), (2, 0), (3, 1)
        ]
        interp.create_polynomial(data_points)


if __name__ == '__main__':
    unittest.main()
