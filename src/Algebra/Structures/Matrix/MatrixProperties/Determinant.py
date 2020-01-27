from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult, MatrixProperty
from src.Algebra.Structures.Matrix.MatrixProperties.Triangular import Triangular


class Determinant(MatrixProperty):

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        triangular_property = matrix.evaluate_property(Triangular())
