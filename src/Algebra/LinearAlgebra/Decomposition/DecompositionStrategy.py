from abc import ABC, abstractmethod

from Core.Lina.VectorFactory import VectorFactory


class DecompositionStrategy(ABC):

    def calculate_determinant(self, matrix):
        raise NotImplementedError()

    def solve(self, matrix, target_vector):
        if target_vector == 0:
            target_vector = VectorFactory.null_vector(matrix.row_count)
        return self._solve(matrix, target_vector)

    @abstractmethod
    def _solve(self, matrix, target_vector):
        pass

    @abstractmethod
    def decompose(self, matrix):
        pass
