from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Inverse(MatrixProperty):
    """
    A * A^-1 = I => A^-1 inverse Matrix zu A
    """

    def _evaluate(self, matrix: Matrix):
        raise NotImplementedError()
