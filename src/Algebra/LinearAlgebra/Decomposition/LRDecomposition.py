import numpy as np

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.Substitution import substitute_backwards
from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.Algebra.Structures import Matrix
from src.Algebra.Structures.Matrix.MatrixFactory import MatrixFactory


class LRDecomposition(DecompositionStrategy):

    def solve(self, matrix, target_vector):
        l, r = self.decompose(matrix)
        return substitute_backwards(r, LRDecomposition.invert_elimination_matrix(l) * target_vector)

    @classmethod
    def create_column_elimination_matrix(cls, matrix, column):
        elimination_matrix = np.zeros((matrix.row_count, matrix.column_count))
        for i in range(column + 1, matrix.row_count):
            elimination_matrix[i, column] = matrix[i, column] / matrix[column, column]
        return MatrixFactory().create_identity_matrix(matrix.column_count) - Matrix(elimination_matrix)

    @classmethod
    def invert_elimination_matrix(cls, matrix, j=None):
        m = matrix.matrix_vectors
        if j is None:
            for i in range(0, matrix.row_count):
                for j in range(i + 1, matrix.row_count):
                    m[i, j] = -m[i, j]
        else:
            for i in range(j + 1, matrix.row_count):
                m[i, j] = -m[i, j]
        return Matrix(m)

    def decompose(self, matrix: Matrix):
        left = MatrixFactory().create_identity_matrix(matrix.row_count)
        for j in range(0, matrix.column_count - 1):
            elimination_matrix = LRDecomposition.create_column_elimination_matrix(matrix, j)
            matrix = elimination_matrix * matrix
            left = left * LRDecomposition.invert_elimination_matrix(elimination_matrix, j)
        return left, matrix
