import numpy

from src.AlgebraicStructures.Matrix.Matrix import Matrix
from tests.MatrixTests import Matrices as m


u_triangular = [

]

l_triangular = [

]

diagonal = [

]

positive_definite = {
m.spd_3x3_1, m.spd_3x3_2, m.spd_3x3_3
}

symmetric = {
m.spd_3x3_1, m.spd_3x3_2, m.spd_3x3_3
}

regular = {
    *positive_definite, *symmetric
}
def create_target_vector(size):
    data = numpy.random.randint(-100, 100, ((size, 1)))
    return Matrix(data)