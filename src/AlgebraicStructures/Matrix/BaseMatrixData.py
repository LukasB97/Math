from abc import ABC

import numpy
from numpy import array


class BaseMatrixData(ABC):
    matrix_vectors: array = None
    data_type: type = None

    def __init__(self, matrix_vectors, *args, **kwargs):
        if (data_type:= kwargs.get("data_type")) is None:
            data_type = float
        self.data_type = data_type
        if (value_creator:= kwargs.get("value_creator")) is not None:
            c = numpy.empty(matrix_vectors.shape, dtype=self.value_type)
            for i in range(len(c)):
                for j in range(len(c[0])):
                    c[i, j] = value_creator(matrix_vectors[i][j])
            matrix_vectors = c
        self.matrix_vectors = numpy.array(matrix_vectors)

    def __repr__(self):
        return str(self.matrix_vectors)

    @property
    def value_type(self) -> type:
        return self.data_type

    @property
    def row_count(self):
        return len(self.matrix_vectors)

    @property
    def column_count(self):
        return len(self.matrix_vectors[0])

    def __setitem__(self, key, value):
        raise ValueError()

    def __eq__(self, other):
        try:
            for i in range(self.row_count):
                for j in range(self.column_count):
                    if self.matrix_vectors[i, j] != other.matrix_vectors[i, j]:
                        return False
            return True
        except IndexError:
            return False
