from src.Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition

from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Determinant(MatrixProperty):

    def __init__(self, decomposition_algorithm=QRDecomposition()):
        super().__init__()
        self.decomposition = decomposition_algorithm

    def _evaluate(self, matrix: Matrix):
        return self.decomposition.calculate_determinant(matrix)
