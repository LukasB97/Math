from math import sqrt

from src.Decomposition import DecompositionStrategy
from src.Decomposition.QRDecomposition import QRDecomposition


class SingularValueDecomposition(DecompositionStrategy):

    def get_singular_values(self, triangular_matrix):
        singular_values = []
        for i in range(triangular_matrix.row_count):
            singular_values.append(sqrt(triangular_matrix[i, i]))
        return singular_values

    def decompose(self, matrix):
        ATA = matrix.transpose() * matrix
        Q, R = ATA.deccompose(QRDecomposition())
        singular_values = self.get_singular_values(R)

        return L, L.transpose()

    @classmethod
    def calc_lower_triangle(cls, A, L, i, j):
        series = 0
        for k in range(j):
            series += L[i][k] * L[j][k]
        return (1 / L[j][j]) * (A[i][j] - series)

    @classmethod
    def calc_diagonal_elem(cls, A, L, i, j):
        series = 0
        for k in range(i):
            series += L[i][k] ** 2
        return sqrt(A[i][i] - series)
