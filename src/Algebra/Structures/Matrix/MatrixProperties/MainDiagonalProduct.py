
from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class MainDiagonalProduct(MatrixProperty):

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        diagonal_product = 1
        for i in range(matrix.row_count):
            if i == matrix.column_count:
                break
            diagonal_product *= matrix[i, i]
        return diagonal_product
