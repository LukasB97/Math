from abc import ABC

import numpy
from numpy import array


class BaseMatrixData(ABC):
    matrix_vectors: array = None
    dtype: type = None

    def __init__(self, matrix_vectors, dtype=None, value_factory=None, preserve_dt=False):
        self.preserve_dt = preserve_dt
        if dtype is None:
            dtype = float
        if value_factory is not None:
            c = numpy.empty((len(matrix_vectors[0]), len(matrix_vectors)), dtype=dtype)
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i, j] = value_factory(matrix_vectors[i][j])
            matrix_vectors = c
        self.dtype = dtype
        self.matrix_vectors = numpy.array(matrix_vectors, dtype=dtype)

    def __repr__(self):
        return str(self.matrix_vectors)

    @property
    def value_type(self) -> type:
        return self.dtype

    # @property
    # def data_representation(self):
    #     pass

    @property
    def row_count(self) -> int:
        return len(self.matrix_vectors)

    @property
    def column_count(self) -> int:
        return len(self.matrix_vectors[0])

    def __setitem__(self, key, value):
        raise ValueError()

    def __eq__(self, other):
        try:
            for i in range(self.row_count):
                for j in range(self.column_count):
                    if not self.value_equality(self.matrix_vectors[i, j], other.matrix_vectors[i, j]):
                        return False
            return True
        except (IndexError, AttributeError):
            return False

    def value_equality(self, a, b) -> bool:
        return numpy.equal(a, b)
