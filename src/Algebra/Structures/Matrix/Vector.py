import numpy

from src.Algebra.Structures.Function.Norm import Norm
from src.Algebra.Structures.Matrix.Matrix import Matrix


class Vector(Matrix):

    def __init__(self, values):
        values = numpy.asarray(values)
        if len(values.shape) == 1:
            values = values.reshape((1, len(values)))
        super().__init__(values)

    def create_normed_vector(self, norm=Norm.euclidean_norm):
        new_vector = self.matrix_vectors * (1 / norm(self))
        return self.create(new_vector)
