import unittest

from Core.Factories.MatrixStructureFactory import MatrixStructureFactory
from src.Algebra.Structures.Matrix.Matrix import Matrix
from Core.Lina.MatrixFactory import MatrixFactory
from tests.MathTests.AlgebraTests.MatrixTests import MatrixCollection


class MatrixStructureFactoryTestCase(unittest.TestCase):

    def test_parse_replacement(self):
        fac = MatrixStructureFactory()
        "{1,2,3"
        res = fac._replacements()



    def test_parse(self):
        for matrix in MatrixCollection.coll:
            matrix = Matrix(matrix)
            self.create_column_vector(matrix)
            self.create_row_vector(matrix)



if __name__ == '__main__':
    unittest.main()
