import numpy

from src.AlgebraicStructures.Matrix import Matrix
from src.AlgebraicStructures.Matrix.MatrixProperties import PropertyResult
from src.AlgebraicStructures.Matrix.MatrixProperties.MatrixProperty import MatrixProperty


class MatrixExtension(MatrixProperty):

    def __init__(self, size, start=True):
        self.size = size
        self.start = start

    def evaluate(self, matrix: Matrix) -> PropertyResult:
        vectors = numpy.zeros((matrix.row_count + self.size, matrix.column_count + self.size))
        for i in range(matrix.row_count):
            for j in range(matrix.column_count):
                vectors[i + self.size, j + self.size] = matrix[i, j]
        return Matrix.Matrix(vectors)
