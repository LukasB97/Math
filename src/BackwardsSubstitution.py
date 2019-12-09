import numpy

from src.AlgebraicStructures.Matrix.Matrix import Matrix


def substitute_backwards(a, b):
    x = numpy.zeros((b.get_row_count, 1))
    for i in range(b.get_row_count - 1, -1, -1):
        row_sum = 0
        for j in range(b.get_row_count - 1, i - 1, -1):
            row_sum += x[j, 0] * a[i, j]
        to_add = b[i, 0] - row_sum
        x[i, 0] = to_add / a[i, i]
    return Matrix(x)
