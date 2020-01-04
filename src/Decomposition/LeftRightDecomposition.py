from src.ElementarMatrix import create_frobenius_matrix

from src.AlgebraicStructures.Matrix import Matrix
from src.Decomposition.DecompositionStrategy import DecompositionStrategy
from src.AlgebraicStructures.Matrix.MatrixFactory import MatrixFactory


class LeftRightDecomposition(DecompositionStrategy):

    def __init__(self, pivot_strategy):
        pass

    def decompose(self, matrix: Matrix):
        input_matrix = matrix.copy()
        left = MatrixFactory().create_identity_matrix(matrix.row_count)
        for j in range(matrix.column_count):
            frobenius_j_elimination = create_frobenius_matrix(input_matrix, j, j)
            input_matrix = frobenius_j_elimination * input_matrix
            left = left * frobenius_j_elimination.invert()
        return left, left.invert() * matrix
