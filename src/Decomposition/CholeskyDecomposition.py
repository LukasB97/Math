from math import sqrt

from numpy import zeros

from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.Decomposition.DecompositionStrategy import DecompositionStrategy


class CholeskyDecomposition(DecompositionStrategy):


    def decompose(self, matrix):
        L = zeros((matrix.get_row_count, matrix.get_row_count))
        for j in range(matrix.get_row_count):
            for i in range(matrix.get_row_count):
                if i < j:
                    L[i][j] = 0
                elif i == j:
                    L[i][j] =  CholeskyDecomposition.calc_diagonal_elem(matrix, L, i, j)
                else:
                    L[i][j] = CholeskyDecomposition.calc_lower_triangle(matrix, L, i, j)
        L = Matrix(L)
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

