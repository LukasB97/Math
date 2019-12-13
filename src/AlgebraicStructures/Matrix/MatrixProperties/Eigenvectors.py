import numpy

from src import BackwardsSubstitution
from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.Eigenvalues import Eigenvalues
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty
from src.Decomposition.QRDecomposition import QRDecomposition
from src.MatrixFactory import MatrixFactory


class Eigenvectors(MatrixProperty):

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        eigenvalues = matrix.evaluate_property(Eigenvalues())
        b = Matrix(numpy.zeros((matrix.get_row_count, 1)))
        eigenvectors = []
        for eigenvalue in eigenvalues:
            m = matrix - (eigenvalue * MatrixFactory().create_identity_matrix(matrix.get_row_count))
            r, q = m.decompose(QRDecomposition())
            eigenvectors.append(BackwardsSubstitution.substitute_backwards(r, q.transpose() * b))
        return eigenvectors