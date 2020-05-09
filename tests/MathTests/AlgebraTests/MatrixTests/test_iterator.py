import unittest

from src.Algebra.Structures.Matrix.Iterator.MatrixIterator import MatrixIterator


class IteratorTests(unittest.TestCase):

    def _test(self, iterator, expected_sequence):
        i = 0
        for entry in iterator:
            self.assertEqual(entry, expected_sequence[i])
            i += 1

    def test_mod_2(self):
        def fn(i, j):
            return i % 2 == 0 and j % 2 == 0

        it = MatrixIterator(fn, 4, 4)
        expected = [(0, 0), (0, 2), (2, 0), (2, 2)]
        self._test(it, expected)
        it = MatrixIterator(fn, 4, 4, False)
        expected = [(0, 0), (2, 0), (0, 2), (2, 2)]
        self._test(it, expected)


if __name__ == '__main__':
    unittest.main()
