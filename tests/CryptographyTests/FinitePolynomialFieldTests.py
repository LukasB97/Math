import unittest

from src.BackwardsSubstitution import substitute_backwards

from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from src.Algebra.Structures import Matrix


class FinitePolynomialFieldTests(unittest.TestCase):

    def test_equal(self):
        matrix_a = Matrix(
            [
                [1, 3, 2],
                [-5, 3, -3.0],
                [5, 7.0, 1]
            ]
        )
        matrix_b = Matrix(
            [
                [1.0, 3, 2.0],
                [-5, 3, -3],
                [5, 7.0, 1]
            ]
        )
        self.assertEqual(matrix_a, matrix_b)

    def test_transpose(self):
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
        self.assertEqual(matrix.transpose(), transposed_matrix)

    def test_householder(self):
        matrix = Matrix(
            [
                [1, 3, 6],
                [9, 3, -6],
                [5, 8, 1]
            ]
        )
        q, r = matrix.decompose(QRDecomposition())
        print(r)
        print(q)
        print(q * q.transpose())
        print(q * r)

    def test_lr(self):
        matrix = Matrix(
            [
                [1, 3, 6],
                [9, 3, -6],
                [5, 8, 1]
            ]
        )
        b = Matrix(
            [
                [3],
                [4],
                [5]
            ]
        )
        q, r = matrix.decompose(QRDecomposition())
        print(substitute_backwards(r, q.transpose() * b))


if __name__ == '__main__':
    unittest.main()
