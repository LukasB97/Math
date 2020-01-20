import numpy

from src import Substitution
from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixFactory import MatrixFactory
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult
from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm import QRAlgorithm
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Eigenvectors(MatrixProperty):

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        eigenvalues = matrix.evaluate_property(QRAlgorithm())
        b = Matrix(numpy.zeros((matrix.row_count, 1)))
        eigenvectors = []
        for eigenvalue in eigenvalues:
            m = matrix - (eigenvalue * MatrixFactory().create_identity_matrix(matrix.row_count))
            r, q = m.decompose(QRDecomposition())
            eigenvectors.append(Substitution.substitute_backwards(r, q.transpose() * b))
        return eigenvectors
