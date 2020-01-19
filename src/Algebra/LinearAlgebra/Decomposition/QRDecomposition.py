from math import sqrt

import numpy

from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.Algebra.Structures import Matrix
from src.Algebra.Structures.Function.Norm import Norm
from src.Algebra.Structures.Matrix.MatrixFactory import MatrixFactory
from src.Substitution import substitute_backwards


class QRDecomposition(DecompositionStrategy):

    def solve(self, matrix, target_vector):
        q, r = self.decompose(matrix)
        return substitute_backwards(r, q.transpose() * target_vector)

    def create_householder_matrix(self, to_project):
        """
        :param to_project:
        :return:
        """
        i = MatrixFactory().create_identity_matrix(to_project.row_count)
        unit_vector = MatrixFactory.create_unit_vector(to_project.row_count, 0)
        orthogonal_projection = to_project + numpy.sign(to_project[0, 0]) * Norm.euclidean_norm(
            to_project) * unit_vector
        orthogonal_projection = orthogonal_projection * (1 / Norm.euclidean_norm(orthogonal_projection))
        res = i - 2 * orthogonal_projection * orthogonal_projection.transpose()
        return res

    def create_householder_reflection(self, to_project, project_onto):
        assert Norm.euclidean_norm(project_onto) != 0
        assert Norm.euclidean_norm(to_project) != 0
        return self.create_householder_matrix(to_project)

    def decompose(self, matrix):
        Q = MatrixFactory.create_identity_matrix(size=matrix.row_count)
        for j in range(matrix.column_count - 1):
            e = numpy.zeros((matrix.column_count - j, 1))
            e[0, 0] = 1
            e = Matrix(e)
            h = self.create_householder_reflection(matrix.get_column_vector(j, j), e)
            h = MatrixFactory.build_block_matrix(d=h, row_count=Q.row_count, col_count=Q.row_count)
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
