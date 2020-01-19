from math import sqrt

from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy


class SingularValueDecomposition(DecompositionStrategy):

    def __init__(self, regularization=None):
        self.regularization = regularization

    def solve(self, matrix, target_vector):
        u, d, v = self.decompose(matrix)

    @classmethod
    def get_singular_values(cls, triangular_matrix):
        singular_values = []
        for i in range(triangular_matrix.row_count):
            singular_values.append(sqrt(triangular_matrix[i, i]))
        return singular_values

    def build_diagonal_matrix(self, singular_values):
        pass

    def decompose(self, matrix):
        ATA = matrix.transpose() * matrix
        singular_values = self.get_singular_values(ATA)
        return L, L.transpose(), 2
