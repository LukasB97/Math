from enum import Enum

from src.Algebra.Structures import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Definiteness(Enum):
    NEGATIVE_DEFINITE = 1
    NEGATIVE_SEMI_DEFINITE = 2
    INDEFINITE = 3
    POSITIVE_SEMI_DEFINITE = 4
    POSITIVE_DEFINITE = 5


class DefinitenessProperty(MatrixProperty):

    def _evaluate(self, matrix: Matrix):
        pass
