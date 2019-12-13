from numpy import zeros

from src.AlgebraicStructures.Matrix.Matrix import Matrix


class MatrixFactory:

    def create_identity_matrix(self, size) -> Matrix:
        v = zeros((size, size))
        for i in range(size):
            v[i][i] = 1
        return Matrix(v)
