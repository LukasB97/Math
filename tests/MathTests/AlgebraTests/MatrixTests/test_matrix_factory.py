import unittest

from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Core.Lina.Lina import matrix_factory
from src.Core.Lina.MatrixFactory import MatrixFactory
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection


class MatrixFactoryTestCase(unittest.TestCase):

    def test_parser(self):
        for matrix in MatrixCollection.complete:
            matrix_object = Matrix(matrix)
            matrix_str = str(matrix)
            self.assertEqual(matrix_object, matrix_factory.parse(matrix_str))

    def test_create_identity(self):
        for matrix in MatrixCollection.complete:
            matrix = Matrix(matrix)
            self.assertEqual(matrix, MatrixFactory.identity(matrix.row_count) * matrix)

    def create_row_vector(self, matrix):
        row_vectors = []
        for i in range(matrix.row_count):
            row_vectors.append(matrix.get_row_vector(i))
        created_matrix = MatrixFactory.matrix_of_row_vectors()
        self.assertEqual(created_matrix, matrix)

    def create_column_vector(self, matrix):
        col_vectors = []
        for i in range(matrix.column_count):
            col_vectors.append(matrix.get_column_vector(i))
        created_matrix = MatrixFactory.matrix_of_column_vectors(*col_vectors)
        self.assertEqual(created_matrix, matrix)

    def test(self):
        for matrix in MatrixCollection.complete:
            matrix = Matrix(matrix)
            self.create_column_vector(matrix)
            self.create_row_vector(matrix)


if __name__ == '__main__':
    unittest.main()
