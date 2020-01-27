import numpy

from src.Algebra.Structures.Matrix.Matrix import Matrix
from tests.MathTests.AlgebraTests.MatrixTests import Matrices as m

u_triangular = [

]

l_triangular = [

]

diagonal = [

]

positive_definite = [
    m.spd_3x3_1, m.spd_3x3_2, m.spd_3x3_3, m.spd_5x5_1
]

symmetric = [
    m.spd_3x3_1, m.spd_3x3_2, m.spd_3x3_3
]

regular = [
    *positive_definite, m.reg_4x4_1
]
a = m.spd_3x3_2

all = [
    *regular
]


def create_target_vector(size):
    data = numpy.random.randint(-100, 100, ((size, 1)))
    return Matrix(data)


def intersection(*args, **kwargs):
    res = []
    for l in args:
        for matrix in l:
            interset = True
            for others in args:
                if matrix not in others:
                    interset = False
                    break
            if interset and matrix not in res:
                res.append(matrix)
            interset = True
    return res
