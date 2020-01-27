from abc import abstractmethod
from numbers import Number

from numpy import transpose

from src.Algebra.Structures.Matrix.BaseMatrixData import BaseMatrixData
from src.Core.AbstractFactory import AbstractFactory


class BaseMatrix(BaseMatrixData):
    matrix_factory: AbstractFactory
    matrix_properties: dict

    def __init__(self, matrix_vectors, *args, **kwargs):
        self.matrix_factory = kwargs.get("matrix_factory")
        self.matrix_properties = dict()
        super().__init__(matrix_vectors, *args, **kwargs)

    @abstractmethod
    def scalar_multiplication(self, scalar: Number):
        pass

    @abstractmethod
    def matrix_multiplication(self, right_matrix: 'BaseMatrix') -> 'BaseMatrix':
        pass

    @property
    def is_quadratic(self) -> bool:
        return self.row_count == self.column_count

    def __mul__(self, other):
        if isinstance(other, BaseMatrix):
            return self.matrix_multiplication(other)
        return self.scalar_multiplication(other)

    def __rmul__(self, other):
        return self.scalar_multiplication(other)

    def __add__(self, other):
        if isinstance(other, BaseMatrix):
            if (other.row_count != self.row_count) or (other.column_count != self.column_count):
                raise ValueError("Cannot add matrices of different dimensions")
            return type(self)(self.matrix_vectors + other.matrix_vectors)

    def __sub__(self, other):
        if isinstance(other, BaseMatrix):
            if (other.row_count != self.row_count) or (other.column_count != self.column_count):
                raise ValueError("Cannot add matrices of different dimensions")
            if self.row_count == self.column_count == 1:
                return self[0, 0] - other[0, 0]
            return self.create(self.matrix_vectors - other.matrix_vectors)

    def __repr__(self):
        return str(self.matrix_vectors)

    def __getitem__(self, item: tuple):
        if len(item) == 2:
            return self.matrix_vectors[item[0]][item[1]]
        elif len(item) == 1:
            if self.row_count > 1:
                return self.get_row_vector(item[0])
            return self[0, item[0]]
        raise ValueError()

    def create(self, *args, **kwargs):
        if self.matrix_factory is None:
            return type(self)(*args, **kwargs)
        return self.matrix_factory.create_instance(*args, **kwargs)

    def get_column_vector(self, j, start=0, end=-1):
        if end == -1:
            end = len(self.matrix_vectors)
        return self.create(self.matrix_vectors[:, j][start:end].reshape((end - start, 1)))

    def get_row_vector(self, i, start=0, end=-1):
        if end == -1:
            end = len(self.matrix_vectors[0])
        return self.create(self.matrix_vectors[i][start:end].reshape((1, end - start)))

    def transpose(self) -> 'BaseMatrix':
        return type(self)(transpose(self.matrix_vectors))

    def __hash__(self):
        return hash(self.matrix_vectors.tostring())
