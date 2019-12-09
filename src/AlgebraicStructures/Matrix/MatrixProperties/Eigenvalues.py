from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Eigenvalues(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
