import numpy

from src.AlgebraicStructures.Matrix.Matrix import Matrix


class DiagonalMatrix(Matrix):

    def __init__(self, values: list = None, size=None):
        if size is None:
            size = len(values)
        matrix_vectors = numpy.zeros((size, size))
        for i in range(size):
            matrix_vectors[i, i] = 1 if values is None else values[i]
        super().__init__(matrix_vectors)
