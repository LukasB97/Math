import numpy

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.LESStrategy import LESStrategy
from src.Algebra.Structures.Matrix.Matrix import Matrix


class GaussSeidelMethod(LESStrategy):

    def __init__(self, delta):
        super().__init__()
        self.delta = delta

    def create_state(self, matrix, b, x=None):
        if x is None:
            x = b
        return {
            "matrix": matrix,
            "b": b,
            "x": x
        }

    @staticmethod
    def calculate_single_component(matrix, b, x, new_x, i):
        column_row_product = b[i, 0]
        for j in range(matrix.row_count):
            if j < i:
                column_row_product -= matrix[i, j] * new_x[j, 0]
            elif j > i:
                column_row_product -= matrix[i, j] * x[j, 0]
        return (1 / matrix[i, i]) * column_row_product

    def next_iteration(self, x, b, matrix):
        new_vector = numpy.zeros((matrix.row_count, 1))
        for i in range(matrix.row_count):
            new_vector[i, 0] = self.calculate_single_component(matrix, b, x, new_vector, i)
        return self.create_state(matrix, b, Matrix(new_vector))

    def _evaluate(self, *args, **kwargs):
        pass

    def check_break_condition(self, matrix, x, b, **kwargs):
        difference = (matrix * x) - b
        return difference.transpose() * difference <= self.delta
