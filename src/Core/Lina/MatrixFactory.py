import numpy
from numpy import zeros, random

from Algebra.Structures.Matrix.Vector import Vector
from Core.Factories.MatrixStructureFactory import MatrixStructureFactory
from Core.Lina.VectorFactory import VectorFactory
from src.Algebra.Structures.Matrix.Matrix import Matrix, BaseMatrix
from src.Core.AbstractFactory import AbstractFactory


class MatrixFactory(AbstractFactory):
    std_data_factory: MatrixStructureFactory = MatrixStructureFactory()

    def __init__(self, data_factory=None):
        if data_factory is None:
            data_factory = self.std_data_factory
        self.data_factory = data_factory

    def parse(self, input_to_parse) -> Matrix:
        data = self.data_factory.parse_string(input_to_parse)
        return Matrix(data)

    def create_instance(self, data):
        data = self.data_factory.create_instance(data)
        return Matrix(data)

    def identity(self, size) -> Matrix:
        v = zeros((size, size))
        for i in range(size):
            v[i][i] = 1
        return Matrix(v)

    @classmethod
    def random(cls, row_count, column_count, lower_bound=0, upper_bound=1):
        return Matrix(random.uniform(low=lower_bound, high=upper_bound, size=(row_count, column_count)))

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

    def matrix_of_row_vectors(self, *vectors):
        vector_length = len(VectorFactory.reshape_data(vectors[0], 1))
        matrix_vectors = numpy.zeros((len(vectors), vector_length))
        for i, vector in enumerate(vectors):
            matrix_vectors[i] = VectorFactory.reshape_data(vector, 1)
        return Matrix(matrix_vectors)

    def matrix_of_column_vectors(self, *vectors: Vector):
        return self.matrix_of_row_vectors(*vectors).transpose()
