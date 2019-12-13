from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.AlgebraicStructures.Matrix.MatrixProperties.Triangular import Triangular, TriangularProperty
from src.Decomposition.QRDecomposition import QRDecomposition


class Eigenvalues(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        r = matrix
        triangular_property = matrix.evaluate_property(Triangular())
        if triangular_property is TriangularProperty.NOT_TRIANGULAR:
            q, r = matrix.decompose(QRDecomposition())
        eigenvalues = []
        for i in range(matrix.get_column_count):
            eigenvalues.append(r[i, i])
        return eigenvalues


