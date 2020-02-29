import numpy

from Algebra.Structures.Matrix.Vector import Vector
from Core.AbstractFactory import AbstractFactory
from src.Algebra.Structures.Matrix.Matrix import Matrix


class VectorFactory(AbstractFactory):

    def create_instance(self, values):
        rows = len(values)
        values = numpy.array(values)
        return Vector(values.reshape((rows, 1)))

    @classmethod
    def create_unit_vector(cls, size, i):
        data = numpy.zeros((size, 1))
        data[i, 0] = 1
        return Vector(data)

    @classmethod
    def reshape_data(cls, vector, num_of_axis):
        if isinstance(vector, Matrix):
            vector = vector.matrix_vectors
        vector = numpy.array(vector)
        if len(vector.shape) == num_of_axis:
            return vector
        if len(vector.shape) == 1:
            return vector.reshape((len(vector), 1))
        return vector.reshape(max(vector.shape))

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
