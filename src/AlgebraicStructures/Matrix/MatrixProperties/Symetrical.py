from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class SymmetricProperty(MatrixProperty):

    def evaluate(self, matrix: Matrix):
        if not matrix.is_quadratic:
            return False
        for i in range(matrix.row_count):
            for j in range(i, matrix.row_count):
                if matrix[i, j] != matrix[j, i]:
                    return False
        return True
