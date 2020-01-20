from enum import Enum

from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class TriangularProperty(Enum):
    NOT_TRIANGULAR = 0
    LOWER_TRIANGULAR = 1
    UPPER_TRIANGULAR = 2
    DIAGONAL = 3


class Triangular(MatrixProperty):

    def _evaluate(self, matrix: Matrix) -> TriangularProperty:
        upper_triangular = self.evaluate_upper_triangle(matrix)
        lower_triangular = self.evaluate_lower_triangle(matrix)
        if lower_triangular:
            if upper_triangular:
                return TriangularProperty.DIAGONAL
            return TriangularProperty.LOWER_TRIANGULAR
        if upper_triangular:
            return TriangularProperty.UPPER_TRIANGULAR
        return TriangularProperty.NOT_TRIANGULAR

    def evaluate_upper_triangle(self, matrix: Matrix):
        for i in range(matrix.row_count):
            for j in range(i):
                if not self.is_zero(matrix[i, j]):
                    return False
        return True

    def evaluate_lower_triangle(self, matrix: Matrix):
        for i in range(matrix.row_count):
            for j in range(i + 1, matrix.column_count):
                if not self.is_zero(matrix[i, j]):
                    return False
        return True
