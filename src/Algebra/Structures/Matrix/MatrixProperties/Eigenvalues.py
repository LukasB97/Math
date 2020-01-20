from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult
from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm import EigenvalueStrategy
from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm import QRAlgorithm
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.Algebra.Structures.Matrix.MatrixProperties.Triangular import Triangular, TriangularProperty


class Eigenvalues(MatrixProperty):

    def __init__(self, delta, eigenvalue_algorithm: EigenvalueStrategy = QRAlgorithm()):
        super().__init__(delta)

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        r = matrix
        triangular_property = matrix.evaluate_property(Triangular())
        if triangular_property is TriangularProperty.NOT_TRIANGULAR:
            q, r = matrix.decompose(QRDecomposition())
        eigenvalues = []
        for i in range(matrix.column_count):
            eigenvalues.append(r[i, i])
        return eigenvalues
