import unittest

import numpy

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.GaussSeidelMethod import GaussSeidelMethod
from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.JacobiMethod import JacobiMethod
from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.LESStrategy import LESStrategy
from src.Algebra.Structures.Matrix.UnitTestMatrix import UnitTestMatrix
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection
from tests.MathTests.Settings import precision_digits


class LESTests(unittest.TestCase):
    numpy.set_printoptions(precision=100)

    def solve(self, matrix, strategy: LESStrategy):
        for i in range(20):
            b = MatrixCollection.create_target_vector(matrix.column_count)
            solution_vector = strategy.execute(matrix, b)
            self.assertEqual(matrix * solution_vector, b)

    def test_jacobi(self):
        jacobi = JacobiMethod(0.000000000000001)
        for A in MatrixCollection.intersection(MatrixCollection.positive_definite, MatrixCollection.symmetric):
            A = UnitTestMatrix(A, precision_digits)
            self.solve(A, jacobi)

    def test_gauss_seidel(self):
        jacobi = GaussSeidelMethod(0.000000000000001)
        for A in MatrixCollection.intersection(MatrixCollection.positive_definite, MatrixCollection.symmetric):
            A = UnitTestMatrix(A, precision_digits)
            self.solve(A, jacobi)


if __name__ == '__main__':
    unittest.main()
