import unittest

from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.MatrixProperties import Eigenvectors, Eigenvalues


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


    def test_eigenvectors(self):
        eigenvector_property = Eigenvectors.Eigenvectors()

    def test_eigenvalues(self):
        eigenvalue_property = Eigenvalues.Eigenvalues()
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
