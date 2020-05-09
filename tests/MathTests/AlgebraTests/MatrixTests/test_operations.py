import unittest

import numpy

from src.Algebra.LinearAlgebra import Operations
from src.Core.Lina.VectorFactory import VectorFactory


class OperationTests(unittest.TestCase):
    numpy.set_printoptions(precision=100)

    def _test_scalar_product(self, v1, v2):
        self.assertEqual(Operations.scalar_product(v1, v2), v2.transpose() * v1)

    def test_ss(self):
        pass

    def test_create_orthogonal_vector(self):
        pass

    def test_singular_value(self):
        v1 = VectorFactory.create([1, 0, 0])
        v2 = VectorFactory.create([0, 1, 0])
        self.assertEqual(Operations.create_orthonormal_vector(v1, v2), VectorFactory.create([0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
