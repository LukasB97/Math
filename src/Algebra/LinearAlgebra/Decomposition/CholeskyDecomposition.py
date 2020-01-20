from math import sqrt

from numpy import zeros

from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.Algebra.Structures import Matrix
from src.Substitution import substitute_backwards
from src.Substitution import substitute_forward


class CholeskyDecomposition(DecompositionStrategy):

    def solve(self, matrix, target_vector):
        """
        A = L*Lt => Ax = b <=> Lz = b, Ltx = z
        :param matrix:
        :param target_vector:
        :return:
        """
        lower, upper = self.decompose(matrix)
        z = substitute_forward(lower, target_vector)
        x = substitute_backwards(upper, z)
        return x

    def decompose(self, matrix):
        L = zeros((matrix.row_count, matrix.row_count))
        for j in range(matrix.row_count):
            for i in range(matrix.row_count):
                if i < j:
                    L[i, j] = 0
                elif i == j:
                    L[i, j] = CholeskyDecomposition.calc_diagonal_elem(matrix, L, i)
                else:
                    L[i, j] = CholeskyDecomposition.calc_lower_triangle(matrix, L, i, j)
        L = Matrix(L)
        return L, L.transpose()

    @classmethod
    def calc_lower_triangle(cls, A, L, i, j):
        series = 0
        for k in range(j):
            series += L[i, k] * L[j, k]
        return (1 / L[j, j]) * (A[i, j] - series)

    @classmethod
    def calc_diagonal_elem(cls, A, L, i):
        series = 0
        for k in range(i):
            series += L[i, k] ** 2
        to_square = A[i, i] - series
        if to_square < 0:
            raise ValueError("Matrix is not positive definite")
        return sqrt(to_square)
