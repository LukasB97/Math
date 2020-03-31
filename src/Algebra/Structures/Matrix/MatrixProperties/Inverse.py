from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import PropertyResult
from src.Algebra.Structures.Matrix.MatrixProperties.IsIdentity import IsIdentity
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Inverse(MatrixProperty):
    """
    A * A^-1 = I => A^-1 inverse Matrix zu A
    """

    def _evaluate(self, matrix: Matrix) -> PropertyResult:
        return (matrix.transpose() * matrix).evaluate_property(IsIdentity())
