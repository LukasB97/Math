from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.Algebra.Structures.Matrix.MatrixProperties.Triangular import Triangular, TriangularProperty


class IsIdentity(MatrixProperty):

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        if matrix.evaluate_property(Triangular()) == TriangularProperty.DIAGONAL:
            for i in range(matrix.row_count):
                if matrix[i, i] != 0:
                    return False
            return True
        return False
