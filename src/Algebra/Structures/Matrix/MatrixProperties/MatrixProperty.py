from abc import ABC, abstractmethod

from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult


class MatrixProperty(ABC):

    def __init__(self, delta=0):
        self.delta = delta

    def evaluate(self, matrix):
        prop = matrix.get_property(self)
        if prop is not None:
            return prop
        prop = self._evaluate(matrix)
        matrix.set_property(self, prop)
        return prop

    @abstractmethod
    def _evaluate(self, matrix: Matrix):
        pass

    def value_equality(self, a, b):
        return abs(a - b) <= self.delta

    def is_zero(self, a):
        return abs(a) < self.delta

    def __eq__(self, other):
        return type(self) == type(other)

    def __hash__(self):
        return hash(type(self))
