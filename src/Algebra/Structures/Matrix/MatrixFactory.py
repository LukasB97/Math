from numpy import zeros, random

from src.AbstractFactory import AbstractFactory
from src.Algebra.Structures.Matrix.Matrix import Matrix, BaseMatrix


class MatrixFactory(AbstractFactory):

    def create_instance(self, *args, **kwargs):
        pass

    @classmethod
    def create_identity_matrix(cls, size) -> Matrix:
        v = zeros((size, size))
        for i in range(size):
            v[i][i] = 1
        return Matrix(v)

    @classmethod
    def create_random(cls, rows, columns, lower_bound=0, upper_bound=1):
        return Matrix(random.uniform(low=lower_bound, high=upper_bound, size=(rows, columns)))

    @classmethod
    def build_block_matrix(cls, a=None, b=None, c=None, d=None, row_count=None, col_count=None) -> Matrix:
        assert not (row_count is None or col_count is None)
        arr = zeros((row_count, col_count))
        if a is not None:
            if isinstance(a, BaseMatrix):
                a = a.matrix_vectors
            arr = cls._fill(arr, a, 0, 0)
        if b is not None:
            if isinstance(b, BaseMatrix):
                b = b.matrix_vectors
            arr = cls._fill(arr, b, 0, col_count - len(b[0]))
        if c is not None:
            if isinstance(c, BaseMatrix):
                c = c.matrix_vectors
            arr = cls._fill(arr, c, row_count - len(c), 0)
        if d is not None:
            if isinstance(d, BaseMatrix):
                d = d.matrix_vectors
            arr = cls._fill(arr, d, row_count - len(d), col_count - len(d[0]))
        return Matrix(arr)

    @classmethod
    def _fill(cls, to_fill, fill_with, from_i, from_j):
        for i in range(from_i, from_i + len(fill_with)):
            for j in range(from_j, from_j + len(fill_with[0])):
                to_fill[i, j] = fill_with[i - from_i, j - from_j]
        return to_fill

    @classmethod
    def create_unit_vector(cls, size, i):
        data = zeros((size, 1))
        data[i, 0] = 1
        return Matrix(data)
