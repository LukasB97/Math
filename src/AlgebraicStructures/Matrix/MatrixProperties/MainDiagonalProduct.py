from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class MainDiagonalProduct(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        diagonal_product = 1
        for i in range(matrix.row_count):
            if i == matrix.column_count:
                break
            diagonal_product *= matrix[i, i]
        return diagonal_product
