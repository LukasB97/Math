import numpy

from src import Substitution
from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixFactory import MatrixFactory
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.EigenvalueAlgorithm.QRAlgorithm import QRAlgorithm
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.Decomposition.QRDecomposition import QRDecomposition


class Eigenvectors(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        eigenvalues = matrix.evaluate_property(QRAlgorithm())
        b = Matrix(numpy.zeros((matrix.row_count, 1)))
        eigenvectors = []
        for eigenvalue in eigenvalues:
            m = matrix - (eigenvalue * MatrixFactory().create_identity_matrix(matrix.row_count))
            r, q = m.decompose(QRDecomposition())
            eigenvectors.append(BackwardsSubstitution.substitute_backwards(r, q.transpose() * b))
        return eigenvectors
