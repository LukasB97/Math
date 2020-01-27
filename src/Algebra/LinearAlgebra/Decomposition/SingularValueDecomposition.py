from math import sqrt

from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm.QRAlgorithm import QRAlgorithm
from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy


class SingularValueDecomposition(DecompositionStrategy):

    def __init__(self, regularization=None):
        self.regularization = regularization

    def solve(self, matrix, target_vector):
        u, d, v = self.decompose(matrix)

    @classmethod
    def get_singular_values(cls, regular_matrix):
        eigenvalues = QRAlgorithm(0.001)
        eigenvalues = eigenvalues.evaluate(regular_matrix)
        singular_values = []
        for eigenvalue in eigenvalues:
            singular_values.append(sqrt(eigenvalue))
        return singular_values

    def build_diagonal_matrix(self, singular_values):
        pass

    def decompose(self, matrix):
        ATA = matrix.transpose() * matrix
        singular_values = self.get_singular_values(ATA)
        return L, L.transpose(), 2
