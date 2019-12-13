import unittest

from src.AlgebraicStructures.Matrix.Matrix import Matrix


class MyTestCase(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
