from enum import Enum

from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Definiteness(Enum):
    NEGATIVE_DEFINITE = 1
    NEGATIVE_SEMI_DEFINITE = 2
    INDEFINITE = 3
    POSITIVE_SEMI_DEFINITE = 4
    POSITIVE_DEFINITE = 5


class DefinitenessProperty(MatrixProperty):

    def evaluate(self, matrix: Matrix):
        pass
