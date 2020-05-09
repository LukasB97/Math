from src.Algebra.Structures.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties.IsIdentity import IsIdentity
from src.Algebra.Structures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Orthogonality(MatrixProperty):
    """
    Q^T*Q = I <=> Q orthogonal
    """

    def _evaluate(self, matrix: Matrix) -> bool:
        return (matrix.transpose() * matrix).evaluate_property(IsIdentity())
