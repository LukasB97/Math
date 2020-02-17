import numpy

from Algebra.Structures.Matrix.Vector import Vector
from src.Algebra.Structures.Matrix.Matrix import Matrix


class VectorFactory:

    @classmethod
    def create(cls, values):
        rows = len(values)
        values = numpy.array(values)
        return Vector(values.reshape((rows, 1)))

    @classmethod
    def null_vector(cls, size):
        return Vector(numpy.zeros((size, 1)))

    @classmethod
    def cross_product(cls, v1, v2) -> Matrix:
        pass
