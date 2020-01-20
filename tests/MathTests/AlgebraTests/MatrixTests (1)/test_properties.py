import unittest

from src.Algebra.Structures import Matrix
from src.Algebra.Structures import QRAlgorithm
from src.Algebra.Structures import Eigenvectors
from src.Algebra.Structures.Matrix.MatrixProperties.MainDiagonalProduct import MainDiagonalProduct


class PropertyTests(unittest.TestCase):

    def test_symmetric(self):
        pass

    def test_main_diagonal_product(self):
        matrix_a = Matrix(
            [
                [1, 3, 2, 0],
                [-5, 3, -3.0, 0],
                [5, 7.0, 1, 1]
            ]
        )
        matrix_b = Matrix(
            [
                [-5, 3, 2.0],
                [-5, 3, -3],
                [5, 7.0, 2]
            ]
        )
        self.assertEqual(matrix_a.evaluate_property(MainDiagonalProduct()), 3)
        self.assertEqual(matrix_b.evaluate_property(MainDiagonalProduct()), -30)

    def test_determinant(self):
        matrix = Matrix(
            [
                [1, 3, 6],
                [9, 3, -6],
                [5, 8, 1]
            ]
        )
        transposed_matrix = Matrix(
            [
                [1, 9, 5],
                [3, 3, 8],
                [6, -6, 1]
            ]
        )

    def test_eigenvectors(self):
        matrix = Matrix(
            [
                [1, 3, 6],
                [9, 3, -6],
                [5, 8, 1]
            ]
        )
        print(matrix.evaluate_property(Eigenvectors()))

    def test_eigenvalues(self):
        matrix = Matrix(
            [
                [-2, -4, 2],
                [-2, 1, 2],
                [4, 2, 5]
            ]
        )
        print(matrix.evaluate_property(QRAlgorithm()))


if __name__ == '__main__':
    unittest.main()