from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.Identity import Identity
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class Orthogonality(MatrixProperty):

    """
    Q^T*Q = I <=> Q orthogonal
    """
    def evaluate(self, matrix: Matrix) -> PropertyResult:
        return (matrix.transpose() * matrix).evaluate_property(Identity())
