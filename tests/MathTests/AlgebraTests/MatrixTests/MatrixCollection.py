import numpy

from src.Algebra.Structures.Matrix.Matrix import Matrix
from tests.MathTests.AlgebraTests.MatrixTests import Matrices

u_triangular = [

]

l_triangular = [

]

diagonal = [

]

positive_definite = [
    Matrices.spd_3x3_1, Matrices.spd_3x3_2, Matrices.spd_3x3_3, Matrices.spd_5x5_1
]

symmetric = [
    Matrices.spd_3x3_1, Matrices.spd_3x3_2, Matrices.spd_3x3_3
]

regular = [
    *positive_definite, Matrices.reg_4x4_1
]
a = Matrices.spd_3x3_2

complete = [
    *regular
]


def create_target_vector(size):
    data = numpy.random.randint(-100, 100, (size, 1))
    return Matrix(data)


def intersection(*args):
    res = []
    for collection in args:
        for matrix in collection:
            interset = True
            for others in args:
                if matrix not in others:
                    interset = False
                    break
            if interset and matrix not in res:
                res.append(matrix)
    return res
