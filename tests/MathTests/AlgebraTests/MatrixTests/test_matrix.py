import math
import unittest

from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from src.Algebra.Structures import Matrix
from src.Algebra.Structures import MatrixFactory
from src.Algebra.Structures import Triangular, TriangularProperty


class MatrixTestCase(unittest.TestCase):

    def test_block_matrix(self):
        a = Matrix([
            [1, 2],
            [2, 3]
        ])
        b = Matrix([
            [3, 2, 6],
            [2, 3, -10]
        ])
        c = Matrix([
            [1, 2],
            [2, 3],
            [7, 7]
        ])
        d = Matrix([
            [1, 2, 9],
            [2, 3, 69],
            [56, 2, 67]
        ])
        res = MatrixFactory.build_block_matrix(a=a, b=b, c=c, d=d, row_count=5, col_count=5)
        res1 = Matrix([
            [1, 2, 3, 2, 6],
            [2, 3, 2, 3, -10],
            [1, 2, 1, 2, 9],
            [2, 3, 2, 3, 69],
            [7, 7, 56, 2, 67]

        ])
        self.assertEqual(res, res1)

    def test_equal(self):
        matrix_a = Matrix(
            [
                [1, 3, 2],
                [-5, 3, -3.0],
                [5, 7.0, 1]
            ]
        )
        matrix_a.invert()
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

    def test_one_n(self):
        a = Matrix(
            [[1, 2, 3, 4, 5]]
        )
        print(a * a.transpose())
        print(a.transpose() * a)

    def test_n_n_mul(self):
        a = Matrix(
            [
                [6, 345, 237, 464],
                [3, 8, 2, 7],
                [5, -54, 1, 5],
                [5, 1, 8, 4]
            ]
        )
        b = Matrix(
            [
                [6, -7, 46, 4],
                [3, -5, 2, 7],
                [5, 4, -1, 55],
                [5, -1, 8, 8]
            ]
        )
        self.assertEqual(a * b, Matrix(
            [
                [4576, -1283, 4441, 19186],
                [87, -60, 208, 234],
                [-102, 234, 161, -263],
                [93, -12, 256, 499]
            ]
        ))
        self.assertEqual(
            b * a,
            Matrix(
                [
                    [265, -466, 1486, 2981],
                    [48, 894, 759, 1395],
                    [312, 1866, 1632, 2563],
                    [107, 1293, 1255, 2385]
                ]
            )
        )
        mm = Matrix([
            [0, 2],
            [-1, 1],
            [1, 1]
        ])
        print(mm.transpose() * mm)

    def test_triangular(self):
        matrix_a = Matrix(
            [
                [1, 3, 2],
                [0, 3, -3.0],
                [0, 0, 1]
            ]
        )
        matrix_b = Matrix(
            [
                [1.0, 0, 2.0],
                [-5, 3, 0],
                [5, 7.0, 1]
            ]
        )
        self.assertEqual(matrix_a.evaluate_property(Triangular()), TriangularProperty.UPPER_TRIANGULAR)
        self.assertEqual(matrix_b.evaluate_property(Triangular()), TriangularProperty.NOT_TRIANGULAR)

    def test_ausgleich(self):
        data = [(0, 2.45), (math.pi / 6, 3.1), (math.pi / 3, 3.63), (math.pi / 2, 4.25), (2 * math.pi / 3, 4.7)
            , (math.pi * 5 / 6, 5.1), (math.pi, 6)]
        A = Matrix([
            [data[0][0] ** 2, data[0][0] * math.sin(data[0][0]), 1],
            [data[1][0] ** 2, data[1][0] * math.sin(data[1][0]), 1],
            [data[2][0] ** 2, data[2][0] * math.sin(data[2][0]), 1],
            [data[3][0] ** 2, data[3][0] * math.sin(data[3][0]), 1],
            [data[4][0] ** 2, data[4][0] * math.sin(data[4][0]), 1],
            [data[5][0] ** 2, data[5][0] * math.sin(data[5][0]), 1],
            [data[6][0] ** 2, data[6][0] * math.sin(data[6][0]), 1]
        ]
        )
        b = Matrix([
            [data[0][1]],
            [data[1][1]],
            [data[2][1]],
            [data[3][1]],
            [data[4][1]],
            [data[5][1]],
            [data[6][1]]
        ])
        res = QRDecomposition().solve(A.transpose() * A, A.transpose() * b)
        for p in data:
            print("f(", p[0], ")= ", self.fn(res[0, 0], res[1, 0], res[2, 0], p[0]))
            print("angabe: ", p[1])

    def fn(self, l1, l2, l3, x):
        return l1 * (x ** 2) + l2 * (x * math.sin(x)) + l3


if __name__ == '__main__':
    unittest.main()
