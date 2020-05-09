from math import sqrt

from numpy import zeros

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.Substitution import substitute_backwards
from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.Substitution import substitute_forward
from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MainDiagonalProduct import MainDiagonalProduct


class CholeskyDecomposition(DecompositionStrategy):

    def calculate_determinant(self, matrix):
        l, lt = self.decompose(matrix)
        return MainDiagonalProduct().evaluate(l) ** 2

    def _solve(self, matrix, target_vector):
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
        triangular_matrix = zeros((matrix.row_count, matrix.row_count))
        for j in range(matrix.row_count):
            for i in range(matrix.row_count):
                if i < j:
                    triangular_matrix[i, j] = 0
                elif i == j:
                    triangular_matrix[i, j] = CholeskyDecomposition.calc_diagonal_elem(matrix, triangular_matrix, i)
                else:
                    triangular_matrix[i, j] = CholeskyDecomposition.calc_lower_triangle(matrix, triangular_matrix, i, j)
        triangular_matrix = Matrix(triangular_matrix)
        return triangular_matrix, triangular_matrix.transpose()

    @classmethod
    def calc_lower_triangle(cls, matrix_to_decompose, current_triangular_matrix, i, j):
        series = 0
        for k in range(j):
            series += current_triangular_matrix[i, k] * current_triangular_matrix[j, k]
        return (1 / current_triangular_matrix[j, j]) * (matrix_to_decompose[i, j] - series)

    @classmethod
    def calc_diagonal_elem(cls, matrix_to_decompose, current_triangular_matrix, i):
        series = 0
        for k in range(i):
            series += current_triangular_matrix[i, k] ** 2
        to_square = matrix_to_decompose[i, i] - series
        if to_square < 0:
            raise ValueError("Matrix is not positive definite")
        return sqrt(to_square)
