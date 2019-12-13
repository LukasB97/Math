from dataclasses import dataclass, field
from numbers import Number
from typing import Dict

import numpy
from numpy import array

from src.AlgebraicStructures.Matrix.BaseMatrix import BaseMatrix
from src.Decomposition import DecompositionStrategy

@dataclass(frozen=True, eq=False, repr=False)
class Matrix(BaseMatrix):




    def invert(self):
        pass

    def copy(self) -> 'Matrix':
        return Matrix(self.matrix_vectors)

    def __init__(self, matrix_vectors, value_creator=None, *args, **kwargs):
        if value_creator is not None:
            for i in range(len(matrix_vectors)):
                for j in range(len(matrix_vectors[0])):
                    matrix_vectors[i][j] = value_creator(matrix_vectors[i][j])
        matrix_vectors: array = array(matrix_vectors)
        super().__init__(matrix_vectors, *args, **kwargs)

    def scalar_multiplication(self, scalar: Number):
        return self.new(scalar * self.matrix_vectors)

    def matrix_multiplication(self, right_matrix: 'BaseMatrix') -> 'BaseMatrix':
        #if not isinstance(right_matrix.get_value_type, Number):
       #     c = numpy.empty((self.get_row_count, right_matrix.get_column_count), dtype=type(right_matrix[0, 0]))
       # else:
        c = numpy.zeros((self.get_row_count, right_matrix.get_column_count))
        for new_row_index in range(self.get_row_count):
            for new_col_index in range(right_matrix.get_column_count):
                row_col_sum = None
                for b_col_index in range(right_matrix.get_row_count):
                    if row_col_sum is None:
                        row_col_sum = self[new_row_index, b_col_index] * right_matrix[b_col_index, new_col_index]
                    else:
                        row_col_sum += self[new_row_index, b_col_index] * right_matrix[b_col_index, new_col_index]
                c[new_row_index][new_col_index] = row_col_sum
        return Matrix(c)

    def vector_multiplication(self, vector):
        pass

    def new(self, matrix_vectors: array = None):
        return Matrix(matrix_vectors)

    def evaluate_property(self, matrix_property):
        # if matrix_property in self.matrix_properties:
        #     return self.matrix_properties[matrix_property]
        # self.matrix_properties[matrix_property] = matrix_property.evaluate(self.copy())
        return matrix_property.evaluate(self.copy())

    def decompose(self, decomposition_strategy: DecompositionStrategy):
        return decomposition_strategy.decompose(self.copy())
