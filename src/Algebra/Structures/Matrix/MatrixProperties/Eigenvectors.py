import numpy

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem import Substitution
from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixFactory import MatrixFactory
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult, Eigenvalues
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Eigenvectors(MatrixProperty):

    def __init__(self, eigenvalue_strategy=Eigenvalues.Eigenvalues()):
        super().__init__()
        self.eigenvalue_strategy = eigenvalue_strategy

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        eigenvalues = self.eigenvalue_strategy.evaluate(matrix)
        b = Matrix(numpy.zeros((matrix.row_count, 1)))
        eigenvectors = []
        for eigenvalue in eigenvalues:
            m = matrix - (eigenvalue * MatrixFactory().create_identity_matrix(matrix.row_count))
            r, q = m.decompose(QRDecomposition())
            eigenvectors.append(Substitution.substitute_backwards(r, q.transpose() * b))
        return eigenvectors
