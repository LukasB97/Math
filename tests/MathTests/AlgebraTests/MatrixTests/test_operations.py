import unittest

import numpy

from Algebra.LinearAlgebra import Operations
from Core.Factories.VectorFactory import VectorFactory
from src.Algebra.LinearAlgebra.Decomposition.CholeskyDecomposition import CholeskyDecomposition
from src.Algebra.LinearAlgebra.Decomposition.LRDecomposition import LRDecomposition
from src.Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from src.Algebra.LinearAlgebra.Decomposition.SingularValueDecomposition import SingularValueDecomposition
from src.Algebra.Structures.Matrix.UnitTestMatrix import UnitTestMatrix
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection


class OperationTests(unittest.TestCase):
    numpy.set_printoptions(precision=100)

    def test_singular_value(self):
        v1 = VectorFactory.create([1, 0, 0])
        v2 = VectorFactory.create([0, 1, 0])
        self.assertEqual(Operations.create_orthogonal_vector(v1, v2), VectorFactory.create([0, 0, 1]))


if __name__ == '__main__':
    unittest.main()
