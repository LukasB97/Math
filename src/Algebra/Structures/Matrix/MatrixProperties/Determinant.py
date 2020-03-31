from Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult, MatrixProperty


class Determinant(MatrixProperty):

    def __init__(self, decomposition_algorithm=QRDecomposition):
        self.decomposition = decomposition_algorithm

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        return self.decomposition.calculate_determinant(matrix)
