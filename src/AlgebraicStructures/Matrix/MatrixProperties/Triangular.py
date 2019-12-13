from enum import Enum

from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.AlgebraicStructures.Matrix.MatrixProperties.PropertyResult import PropertyResult


class TriangularProperty(Enum):
    NOT_TRIANGULAR = 0
    LOWER_TRIANGULAR = 1
    UPPER_TRIANGULAR = 2
    DIAGONAL = 3


class Triangular(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> TriangularProperty:
        upper_triangular = Triangular.evaluate_upper_triangle(matrix)
        lower_triangular = Triangular.evaluate_upper_triangle(matrix)
        if lower_triangular:
            if upper_triangular:
                return TriangularProperty.DIAGONAL
            return TriangularProperty.LOWER_TRIANGULAR
        if upper_triangular:
            return TriangularProperty.UPPER_TRIANGULAR
        return TriangularProperty.NOT_TRIANGULAR

    @classmethod
    def evaluate_upper_triangle(cls, matrix: Matrix):
        for i in range(matrix.get_row_count):
            for j in range(matrix.get_column_count):
                if i > j:
                    if matrix[i, j] != 0:
                        return False
        return True

    @classmethod
    def evaluate_lower_triangle(cls, matrix: Matrix):
        for i in range(matrix.get_row_count):
            for j in range(matrix.get_column_count):
                if i < j:
                    if matrix[i, j] != 0:
                        return False
        return True
