from typing import List, Tuple

import numpy

from Algebra.Structures.Matrix.Vector import Vector
from src.Algebra.LinearAlgebra.Algorithms.EquationSystem import Substitution
from src.Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from src.Algebra.Structures.Matrix.Matrix import Matrix
from Core.Lina.MatrixFactory import MatrixFactory
from src.Algebra.Structures.Matrix.MatrixProperties import Eigenvalues
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Eigenpairs(MatrixProperty):

    def __init__(self, eigenvalue_strategy=Eigenvalues.Eigenvalues()):
        super().__init__()
        self.eigenvalue_strategy = eigenvalue_strategy

    def _evaluate(self, matrix: Matrix) -> List[Tuple[Vector, float]]:
        eigenvalues = self.eigenvalue_strategy.evaluate(matrix)
        b = Matrix(numpy.zeros((matrix.row_count, 1)))
        eigenvectors = []
        for eigenvalue in eigenvalues:
            m = matrix - (eigenvalue * MatrixFactory().create_identity_matrix(matrix.row_count))
            r, q = m.decompose(QRDecomposition())
            eigenvectors.append(Substitution.substitute_backwards(r, q.transpose() * b))
        return eigenvectors
