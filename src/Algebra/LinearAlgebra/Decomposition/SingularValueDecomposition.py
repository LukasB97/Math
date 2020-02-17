from math import sqrt
from typing import Tuple, List

import numpy

from Algebra.Structures.Matrix.Matrix import Matrix
from Algebra.Structures.Matrix.MatrixProperties.Eigenvalues import Eigenvalues
from Algebra.Structures.Matrix.MatrixProperties.Eigenvectors import Eigenvectors
from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm.QRAlgorithm import QRAlgorithm
from src.Algebra.LinearAlgebra.Decomposition.DecompositionStrategy import DecompositionStrategy


class SingularValueDecomposition(DecompositionStrategy):

    def __init__(self, eigenvector_strategy: Eigenvectors = None, regularization=None):
        self.eigenector_strategy = eigenvector_strategy
        self.regularization = regularization

    def solve(self, matrix, target_vector):
        u, d, v = self.decompose(matrix)

    def build_u(self):
        pass

    def get_singular_values(self, regular_matrix) -> List[float]:
        eigenvalues = Eigenvalues()
        eigenvalues = eigenvalues.evaluate(regular_matrix)
        singular_values = []
        for eigenvalue in eigenvalues:
            singular_values.append(sqrt(eigenvalue))
        return singular_values.sort(reverse=True)



    def build_diagonal_matrix(self, singular_values, size: Tuple[int]):
        matrix = numpy.zeros(size)
        for i in range(len(singular_values)):
            matrix[i, i] = singular_values[i]
        return Matrix(matrix)


    def build_u(self, matrix, eigenvectors):
        """
        u_n = (1 / singular_value_n) * A * eigenvector_n
        """
        vectors = []
        for eigenpair in eigenvectors:
            vector = (1 / sqrt(eigenpair[1])) * matrix * eigenpair[0]
            vectors.append(vector)
        return Matrix(*vectors)

    def build_eigenbasis(self, eigenpairs) -> Matrix:
        pass



    def decompose(self, matrix):
        matrix_t_matrix = matrix.transpose() * matrix
        eigenvectors = self.eigenector_strategy.evaluate(matrix_t_matrix)
        eigenvectors.sort()
        us = self.build_u(eigenvectors)
        singular_values = self.get_singular_values(matrix_t_matrix)
        diagonal_matrix = self.build_diagonal_matrix(singular_values=singular_values, size=matrix.shape)
        eigenbasis = self.build_eigenbasis(eigenvectors)
        return us, diagonal_matrix, eigenbasis.transpose()
