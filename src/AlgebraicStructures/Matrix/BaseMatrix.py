from numpy import array, transpose
from numbers import Number
from abc import ABC, abstractmethod



class BaseMatrix(ABC):

    @property
    def get_row_count(self):
        return len(self.matrix_vectors)
    
    @property
    def get_column_count(self):
        return len(self.matrix_vectors[0])

    def get_column_vector(self, j, start=0, end=-1):
        if end == -1:
            end = len(self.matrix_vectors)
        b= self.new(self.matrix_vectors[:, j][start:end].reshape((end-start, 1)))
        return b

    def get_row_vector(self, i, start=0, end=-1):
        if end == -1:
            end = len(self.matrix_vectors[0])
        return self.new(self.matrix_vectors[i][start:end].reshape((1, end - start)))

    @abstractmethod
    def scalar_multiplication(self, scalar: Number):
        pass

    @abstractmethod
    def matrix_multiplication(self, right_matrix: 'BaseMatrix') -> 'BaseMatrix':
        pass

    @abstractmethod
    def vector_multiplication(self, vector):
        pass

    @abstractmethod
    def invert(self):
        pass

    @abstractmethod
    def new(self, matrix_vectors: array = None):
        pass

    @abstractmethod
    def copy(self):
        pass

    def __getitem__(self, item: tuple):
        if len(item) == 2:
            return self.matrix_vectors[item[0]][item[1]]
        elif len(item) == 1:
            if self.get_row_count > 1:
                return self.get_row_vector(item[0])
            return self[0, item[0]]
        raise ValueError()

    def __setitem__(self, key, value):
        raise PermissionError("const")

    def __init__(self, matrix_vectors, value_factory, *args, **kwargs):
        if value_factory is not None:
            for i in range(len(matrix_vectors)):
                for j in range(len(matrix_vectors[0])):
                    matrix_vectors[i][j] = value_factory.create(matrix_vectors[i][j])
        self.matrix_vectors: array = array(matrix_vectors)
        
    def __mul__(self, other):
        if self.get_row_count == self.get_column_count == 1:
            return self[0, 0] * other
        if isinstance(other, Number):
            return self.scalar_multiplication(other)
        if isinstance(other, BaseMatrix):
            return self.matrix_multiplication(other)
        return self.vector_multiplication(other.transpose().transpose())

    def __rmul__(self, other):
        if self.get_row_count == self.get_column_count == 1:
            return other * self[0, 0]
        if isinstance(other, Number):
            return self.scalar_multiplication(other)
        return self.vector_multiplication()

    def __add__(self, other):
        if self.get_row_count == self.get_column_count == 1:
            return self[0, 0] + other
        if isinstance(other, BaseMatrix):
            if (other.get_row_count != self.get_row_count) or (other.get_column_count != self.get_column_count):
                raise ValueError("Cannot add matricies of different dimensions")
            return self.new(self.matrix_vectors + other.matrix_vectors)

    def __sub__(self, other):
        if self.get_row_count == self.get_column_count == 1:
            return self[0, 0] - other
        if isinstance(other, BaseMatrix):
            if (other.get_row_count != self.get_row_count) or (other.get_column_count != self.get_column_count):
                raise ValueError("Cannot add matricies of different dimensions")
            return self.new(self.matrix_vectors - other.matrix_vectors)

    def __eq__(self, other):
        try:
            for i in range(self.get_row_count):
                for j in range(self.get_column_count):
                    if self[i, j] != other[i, j]:
                        return False
            return True
        except Exception:
            return False

    def __repr__(self):
        return str(self.matrix_vectors)

    def transpose(self) -> 'Matrix':
        return self.new(transpose(self.matrix_vectors))

