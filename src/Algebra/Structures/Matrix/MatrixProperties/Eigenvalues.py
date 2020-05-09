from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm.EigenvalueStrategy import EigenvalueStrategy
from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm.QRAlgorithm import QRAlgorithm
from src.Algebra.Structures.Matrix import Matrix

from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Eigenvalues(MatrixProperty):

    def __init__(self, eigenvalue_strategy: EigenvalueStrategy = QRAlgorithm()):
        self.strategy = eigenvalue_strategy
        super().__init__()

    def _evaluate(self, matrix: Matrix):
        raise NotImplementedError()
        # return self.strategy.execute(matrix)
