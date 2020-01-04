from enum import Enum

from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class TriangularProperty(Enum):
    NOT_TRIANGULAR = 0
    LOWER_TRIANGULAR = 1
    UPPER_TRIANGULAR = 2
    DIAGONAL = 3


class Triangular(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> TriangularProperty:
        upper_triangular = Triangular.evaluate_upper_triangle(matrix)
        lower_triangular = Triangular.evaluate_lower_triangle(matrix)
        if lower_triangular:
            if upper_triangular:
                return TriangularProperty.DIAGONAL
            return TriangularProperty.LOWER_TRIANGULAR
        if upper_triangular:
            return TriangularProperty.UPPER_TRIANGULAR
        return TriangularProperty.NOT_TRIANGULAR

    @classmethod
    def evaluate_upper_triangle(cls, matrix: Matrix):
        for i in range(matrix.row_count):
            for j in range(i):
                if round(matrix[i, j], 5) != 0:
                    return False
        return True

    @classmethod
    def evaluate_lower_triangle(cls, matrix: Matrix):
        for i in range(matrix.row_count):
            for j in range(i + 1, matrix.column_count):
                if round(matrix[i, j], 5) != 0:
                    return False
        return True
