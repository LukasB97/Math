import unittest

import numpy

from src.Algebra.LinearAlgebra.Decomposition.CholeskyDecomposition import CholeskyDecomposition
from src.Algebra.LinearAlgebra.Decomposition.LRDecomposition import LRDecomposition
from src.Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from src.Algebra.LinearAlgebra.Decomposition.SingularValueDecomposition import SingularValueDecomposition
from src.Algebra.Structures.Matrix.UnitTestMatrix import UnitTestMatrix
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection
from tests.MathTests.Settings import precision_digits


class DecompositionTests(unittest.TestCase):
    numpy.set_printoptions(precision=100)

    def decomposition(self, matrix, decomposition, test_solve=True):
        decomposed_matrices = decomposition.decompose(matrix)
        decomposed_product = decomposed_matrices[0] * decomposed_matrices[1]
        for i in range(2, len(decomposed_matrices)):
            decomposed_product *= decomposed_matrices[i]
        self.assertEqual(matrix, decomposed_product)
        if not test_solve:
            return
        for i in range(20):
            b = MatrixCollection.create_target_vector(matrix.column_count)
            solution_vector = decomposition.solve(matrix, b)
            self.assertEqual(matrix * solution_vector, b)

    def test_qr(self):
        decomposition = QRDecomposition()
        for matrix in MatrixCollection.regular:
            matrix = UnitTestMatrix(matrix, precision_digits)
            self.decomposition(matrix, decomposition)

    def test_lr(self):
        decomposition = LRDecomposition()
        for matrix in MatrixCollection.regular:
            matrix = UnitTestMatrix(matrix, precision_digits)
            self.decomposition(matrix, decomposition)

    def test_cholesky(self):
        decomposition = CholeskyDecomposition()
        for matrix in MatrixCollection.intersection(MatrixCollection.positive_definite, MatrixCollection.symmetric):
            matrix = UnitTestMatrix(matrix, precision_digits)
            self.decomposition(matrix, decomposition)

    def test_singular_value(self):
        decomposition = SingularValueDecomposition()
        for matrix in MatrixCollection.complete:
            matrix = UnitTestMatrix(matrix, precision_digits)
            self.decomposition(matrix, decomposition)


if __name__ == '__main__':
    unittest.main()
