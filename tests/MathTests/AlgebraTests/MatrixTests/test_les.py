import unittest

import numpy

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.GaussSeidelMethod import GaussSeidelMethod
from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.JacobiMethod import JacobiMethod
from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.LESStrategy import LESStrategy
from src.Algebra.Structures.Matrix.UnitTestMatrix import UnitTestMatrix
from src.Algebra.LinearAlgebra.Decomposition import CholeskyDecomposition
from src.Algebra.LinearAlgebra.Decomposition import LRDecomposition
from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection


class LESTests(unittest.TestCase):
    numpy.set_printoptions(precision=100)

    def solve(self, matrix, strategy: LESStrategy):
        for i in range(20):
            b = MatrixCollection.create_target_vector(matrix.column_count)
            solution_vector = strategy.execute(matrix, b)
            self.assertEqual(matrix * solution_vector, b)
    #
    # def test_qr(self):
    #     decomposition = QRDecomposition()
    #     for A in MatrixCollection.regular:
    #         A = UnitTestMatrix(A, 10)
    #         self.decomposition(A, decomposition)
    #
    # def test_lr(self):
    #     decomposition = LRDecomposition()
    #     for A in MatrixCollection.regular:
    #         A = UnitTestMatrix(A, 10)
    #         self.decomposition(A, decomposition)
    #
    # def test_cholesky(self):
    #     decomposition = CholeskyDecomposition()
    #     for A in MatrixCollection.intersection(MatrixCollection.positive_definite, MatrixCollection.symmetric):
    #         A = UnitTestMatrix(A, 10)
    #         self.decomposition(A, decomposition)

    def test_jacobi(self):
        jacobi = JacobiMethod(0.000000000000001)
        for A in MatrixCollection.intersection(MatrixCollection.positive_definite, MatrixCollection.symmetric):
            A = UnitTestMatrix(A, 10)
            self.solve(A, jacobi)

    def test_gauss_seidel(self):
        jacobi = GaussSeidelMethod(0.000000000000001)
        for A in MatrixCollection.intersection(MatrixCollection.positive_definite, MatrixCollection.symmetric):
            A = UnitTestMatrix(A, 10)
            self.solve(A, jacobi)

        




if __name__ == '__main__':
    unittest.main()
