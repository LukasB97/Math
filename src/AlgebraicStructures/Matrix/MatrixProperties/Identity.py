from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.AlgebraicStructures.Matrix.MatrixProperties.Triangular import Triangular, TriangularProperty


class Identity(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        if matrix.evaluate_property(Triangular()) == TriangularProperty.DIAGONAL:
            for i in range(matrix.get_row_count):
                if matrix[i, i] != 0:
                    return False
            return True
        return False
