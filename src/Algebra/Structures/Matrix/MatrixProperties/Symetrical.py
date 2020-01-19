from src.Algebra.Structures import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class SymmetricProperty(MatrixProperty):

    def _evaluate(self, matrix: Matrix):
        if not matrix.is_quadratic:
            return False
        for i in range(matrix.row_count):
            for j in range(i, matrix.row_count):
                if not self.value_equality(matrix[i, j], matrix[j, i]):
                    return False
        return True
