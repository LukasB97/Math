import unittest

from src.Core.Factories.MatrixStructureFactory import MatrixStructureFactory


class MatrixStructureFactoryTestCase(unittest.TestCase):

    @staticmethod
    def test_parse_replacement():
        fac = MatrixStructureFactory()
        "{1,2,3"


if __name__ == '__main__':
    unittest.main()
