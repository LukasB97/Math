import math

import numpy
from numpy import array

from src.AbstractFactory import AbstractFactory
from src.AlgebraicStructures.Matrix.BaseMatrix import BaseMatrix
from src.Decomposition import DecompositionStrategy


class Matrix(BaseMatrix):

    def invert(self):
        pass

    def copy(self) -> 'Matrix':
        return Matrix(self.matrix_vectors)

    def __init__(self, matrix_vectors, *args, **kwargs):
        super().__init__(matrix_vectors=matrix_vectors, *args, **kwargs)

    def scalar_multiplication(self, scalar):
        return self.create(scalar * self.matrix_vectors)

    def matrix_multiplication(self, right_matrix: 'BaseMatrix') -> 'BaseMatrix':
        c = numpy.empty((self.row_count, right_matrix.column_count), dtype=self.value_type)
        for new_row_index in range(self.row_count):
            for new_col_index in range(right_matrix.column_count):
                row_col_sum = None
                for b_col_index in range(right_matrix.row_count):
                    if row_col_sum is None:
                        row_col_sum = self[new_row_index, b_col_index] * right_matrix[b_col_index, new_col_index]
                    else:
                        row_col_sum += self[new_row_index, b_col_index] * right_matrix[b_col_index, new_col_index]
                c[new_row_index][new_col_index] = row_col_sum
        if len(c) == len(c[0]) == 1:
            return c[0, 0]
        return self.create(c)

    def evaluate_property(self, matrix_property):
        if matrix_property in self.matrix_properties:
            return self.matrix_properties[matrix_property]
        self.matrix_properties[matrix_property] = matrix_property.evaluate(self.copy())
        return self.matrix_properties[matrix_property]

    def decompose(self, decomposition_strategy: DecompositionStrategy):
        return decomposition_strategy.decompose(self.copy())
