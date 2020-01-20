import numpy

from src.Algebra.Structures import Matrix


def substitute_backwards(a, b):
    x = numpy.zeros((b.row_count, 1))
    for i in range(b.row_count - 1, -1, -1):
        row_sum = 0
        for j in range(b.row_count - 1, i - 1, -1):
            row_sum += x[j, 0] * a[i, j]
        to_add = b[i, 0] - row_sum
        x[i, 0] = to_add / a[i, i]
    res = Matrix(x)
    #    assert a * res == b
    return res


def substitute_forward(a, b):
    x = numpy.zeros((b.row_count, 1))
    for i in range(b.row_count):
        row_sum = 0
        for j in range(0, i):
            row_sum += x[j, 0] * a[i, j]
        to_add = b[i, 0] - row_sum
        x[i, 0] = to_add / a[i, i]
    res = Matrix(x)
    assert a * res == b
    return res
