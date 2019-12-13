from math import sqrt

import numpy
from numpy import zeros

from src.AlgebraicStructures.Function.Norm import Norm
from src.AlgebraicStructures.Matrix.DiagonalMatrix import DiagonalMatrix
from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixExtension import MatrixExtension
from src.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.MatrixFactory import MatrixFactory


class QRDecomposition(DecompositionStrategy):

    def create_householder_matrix(self, v):
        i = MatrixFactory().create_identity_matrix(v.get_row_count)
        orthogonal_projection = (2 / ((v.transpose() * v)[0, 0])) * (v * v.transpose())
        return i - orthogonal_projection

    def create_householder_reflection(self, a, e):
        l = Norm.euclidean_norm(a)
        if a[0, 0] < 0:
            l *= (-1)
        v = a + l * e
        v = v * (1 / Norm.euclidean_norm(v))
        return self.create_householder_matrix(v)

    def decompose(self, matrix):
        Q = DiagonalMatrix(size=matrix.get_row_count)
        for j in range(matrix.get_column_count):
            e = numpy.zeros((matrix.get_column_count - j, 1))
            e[0, 0] = 1
            e = Matrix(e)
            h = self.create_householder_reflection(matrix.get_column_vector(j, j), e)
            h = h.evaluate_property(MatrixExtension(j, True))
            for i in range(j):
                h.matrix_vectors[i, i] = 1
            matrix = h * matrix
            Q = h * Q
        return Q.transpose(), matrix

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
