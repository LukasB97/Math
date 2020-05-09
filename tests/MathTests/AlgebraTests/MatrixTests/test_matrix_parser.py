import unittest

from src.Algebra.Structures.Function.Parser.ParseException import ParseException
from src.Core.Lina.MatrixFactory import MatrixFactory


class MatrixParserTestCase(unittest.TestCase):

    def _test_illegal(self, input_to_parse):
        with self.assertRaises(ParseException):
            MatrixFactory().parse(input_to_parse)

    @staticmethod
    def test_illegal():
        pass


if __name__ == '__main__':
    unittest.main()
