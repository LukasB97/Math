import unittest

from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Cryptography.Ciphers.Symmetric.AES import AES
from src.Cryptography.FinitePolynomialField import FinitePolynomialField
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection


class AESTests(unittest.TestCase):

    def test_shift_row(self):
        aes = AES()
        matrix = MatrixCollection.four_x_four[0]
        matrix = Matrix(matrix, value_factory=aes.field_constructor, dtype=FinitePolynomialField, preserve_dt=True)
        self.assertEqual(matrix, aes.revert_shift_row(aes.shift_row(matrix)))


if __name__ == '__main__':
    unittest.main()
