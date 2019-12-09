from abc import ABC, abstractmethod

from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult


class MatrixProperty(ABC):

    @abstractmethod
    def evaluate(self, matrix: Matrix) -> PropertyResult:
        pass