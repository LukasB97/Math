import unittest

from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.Algorithms.LinearAlgebra.ConjugatedGradientMethod import ConjugatedGradientMethod
from src.Decomposition.LRDecomposition import LRDecomposition
from src.Substitution import substitute_backwards
from src.Decomposition.CholeskyDecomposition import CholeskyDecomposition
from src.Decomposition.QRDecomposition import QRDecomposition
from tests.MatrixTests import MatrixCollection


class DecompositionTests(unittest.TestCase):

    def test_decomposition(self, matrix, decomposition, round_digits=None):
        decomposed_matrices = matrix.decompose(decomposition)
        decomposed_product = decomposed_matrices[0] * decomposed_matrices[1]
        for i in range(2, len(decomposed_matrices)):
            decomposed_product *= decomposed_matrices[i]
        if round_digits is not None:
            decomposed_product = round(decomposed_product, round_digits)
        self.assertEqual(matrix, decomposed_product)
        for i in range(20):
            b = MatrixCollection.create_target_vector(matrix.column_count)
            solution_vector = decomposition.solve(matrix, b)
            if round_digits is not None:
                solution_vector = round(solution_vector, round_digits)
            self.assertEqual(matrix * solution_vector, b)

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

    def test_qr(self):
        decomposition = QRDecomposition()
        for A in MatrixCollection.regular:
            self.test_decomposition(A, decomposition, 8)


    def test_lr(self):
        decomposition = LRDecomposition()


    def test_cholesky(self):
        decomposition = CholeskyDecomposition()
        for A in MatrixCollection.positive_definite.intersection(MatrixCollection.symmetric):
            self.test_decomposition(A, decomposition, 8)






if __name__ == '__main__':
    unittest.main()
