import numpy as np

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.Substitution import substitute_backwards
from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MainDiagonalProduct import MainDiagonalProduct
from src.Core.Lina.MatrixFactory import MatrixFactory


class LRDecomposition(DecompositionStrategy):

    def calculate_determinant(self, matrix):
        l, r = self.decompose(matrix)
        return MainDiagonalProduct().evaluate(l) * MainDiagonalProduct().evaluate(r)

    def _solve(self, matrix, target_vector):
        l, r = self.decompose(matrix)
        return substitute_backwards(r, LRDecomposition.invert_elimination_matrix(l) * target_vector)

    @classmethod
    def create_column_elimination_matrix(cls, matrix, column):
        elimination_matrix = np.zeros((matrix.row_count, matrix.column_count), dtype=matrix.dtype)
        for i in range(column + 1, matrix.row_count):
           # print(matrix)
          #  print(matrix[i, column], "/", matrix[column, column], " = ", matrix[i, column] / matrix[column, column])
            elimination_matrix[i, column] = matrix[i, column] / matrix[column, column]
        return MatrixFactory().identity(matrix.column_count) - Matrix(elimination_matrix, dtype=matrix.dtype, preserve_dt=True)

    @classmethod
    def invert_elimination_matrix(cls, matrix, j=None):
        m = np.zeros((matrix.row_count, matrix.column_count), dtype=matrix.dtype)
        if j is None:
            for i in range(0, matrix.row_count):
                for j in range(i + 1, matrix.row_count):
                    m[i, j] = matrix[i, j]
        else:
            for i in range(j + 1, matrix.row_count):
                m[i, j] = matrix[i, j]
        return Matrix(m, dtype=matrix.dtype, preserve_dt=True)

    def decompose(self, matrix: Matrix):
        left = MatrixFactory().identity(matrix.row_count)
        for j in range(0, matrix.column_count - 1):
            elimination_matrix = LRDecomposition.create_column_elimination_matrix(matrix, j)
            matrix = elimination_matrix * matrix
            left = left * LRDecomposition.invert_elimination_matrix(elimination_matrix, j)
        return left, matrix
