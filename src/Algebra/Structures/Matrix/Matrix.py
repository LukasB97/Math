from numbers import Number

import numpy

from src.Algebra.Structures.Matrix.BaseMatrix import BaseMatrix


class Matrix(BaseMatrix):

    def __init__(self, matrix_vectors, *args, **kwargs):
        super().__init__(matrix_vectors=matrix_vectors, *args, **kwargs)

    def get_property(self, prop):
        if prop not in self.matrix_properties:
            return None
        return self.matrix_properties[prop]

    def sum(self, iterator=None):
        if iterator is None:
            return self.matrix_vectors.sum()

    def product(self, iterator):
        res = 1
        for entry in iterator:
            res *= self[entry]
        return res

    def sub_matrix(self, from_i, to_i, from_j, to_j):
        return self.create(self.matrix_vectors[from_i:to_i][from_j: to_j])

    def set_property(self, prop, result):
        assert prop not in self.matrix_properties
        self.matrix_properties[prop] = result

    def scalar_multiplication(self, scalar):
        return self.create(scalar * self.matrix_vectors)

    def get_new_type(self, other_matrix):
        if self.dtype == other_matrix.dtype:
            return self.dtype
        if self.preserve_dt ^ other_matrix.preserve_dt:
            return self.dtype if self.preserve_dt else other_matrix.dtype
        if isinstance(self.dtype, Number) and isinstance(self.dtype, Number):
            if isinstance(self.dtype, complex) or isinstance(other_matrix.dtype, complex):
                return complex
            return float

    def matrix_multiplication(self, right_matrix: 'Matrix') -> 'Matrix':
        c = numpy.empty((self.row_count, right_matrix.column_count), dtype=self.get_new_type(right_matrix))
        for new_row_index in range(self.row_count):
            for new_col_index in range(right_matrix.column_count):
                row_col_sum = 0
                for b_col_index in range(right_matrix.row_count):
                    row_col_sum += self[new_row_index, b_col_index] * right_matrix[b_col_index, new_col_index]
                c[new_row_index][new_col_index] = row_col_sum
        if len(c) == len(c[0]) == 1:
            return c[0, 0]
        return self.create(c, dtype=self.get_new_type(right_matrix))

    def __round__(self, n=6):
        return self.create(numpy.round(self.matrix_vectors, n))

    def __xor__(self, other):
        return self.create(self.matrix_vectors ^ other.matrix_vectors)
