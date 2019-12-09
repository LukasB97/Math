from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import MatrixProperty
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.Triangular import Triangular


class Determinant(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        triangular_property = matrix.evaluate_property(Triangular())
