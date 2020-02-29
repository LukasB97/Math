from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.Algebra.Structures.Matrix.MatrixProperties.TriangularProperty import TriangularProperty, TriangularState


class IsIdentity(MatrixProperty):

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        if matrix.evaluate_property(TriangularProperty()) == TriangularState.DIAGONAL:
            for i in range(matrix.row_count):
                if matrix[i, i] != 0:
                    return False
            return True
        return False
