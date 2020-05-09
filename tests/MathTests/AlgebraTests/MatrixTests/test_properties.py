import unittest

import src.Core.Lina.Properties as Properties
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Algebra.Structures.Matrix.UnitTestMatrix import UnitTestMatrix
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection
from tests.MathTests.Settings import precision_digits


class PropertyTests(unittest.TestCase):

    def test_orthogonality(self):
        for matrix in MatrixCollection.complete:
            matrix = UnitTestMatrix(matrix, precision_digits)
            eigenpairs = Properties.orthogonality.evaluate(matrix)
            for value, vector in eigenpairs:
                stretched_vector = matrix * vector
                self.assertEqual(stretched_vector, vector * value)

    def test_inverse(self):
        for matrix in MatrixCollection.regular:
            matrix = UnitTestMatrix(matrix, precision_digits)
            inverse = Properties.inverse.evaluate(matrix)
            self.assertEqual(matrix, inverse)

    def test_symmetric(self):
        for matrix in MatrixCollection.complete:
            matrix_object = Matrix(matrix)
            symmetric = Properties.symmetrical.evaluate(matrix_object)
            self.assertEqual(symmetric, matrix in MatrixCollection.symmetric)

    def test_eigenpairs(self):
        for matrix in MatrixCollection.regular:
            matrix = Matrix(matrix, precision_digits)
            eigenpairs = Properties.eigenpairs.evaluate(matrix)
            for value, vector in eigenpairs:
                stretched_vector = matrix * vector
                self.assertEqual(stretched_vector, vector * value)

    def test_eigenvalues(self):
        for matrix in MatrixCollection.regular:
            matrix = Matrix(matrix, precision_digits)
            eigenpairs = Properties.eigenvalues.evaluate(matrix)
            for value, vector in eigenpairs:
                stretched_vector = matrix * vector
                self.assertEqual(stretched_vector, vector * value)


if __name__ == '__main__':
    unittest.main()
