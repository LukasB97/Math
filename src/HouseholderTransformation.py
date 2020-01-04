from src.AlgebraicStructures.Function.Norm import Norm
from src.AlgebraicStructures.Matrix.MatrixFactory import MatrixFactory


def create_householder_matrix(v):
    i = MatrixFactory().create_identity_matrix(v.row_count)
    orthogonal_projection = (2 / ((v.transpose() * v)[0, 0])) * (v * v.transpose())
    return i - orthogonal_projection


def create_householder_reflection(a, e):
    l = Norm.euclidean_norm(a)
    if a[0, 0] < 0:
        l *= (-1)
    v = a - l * e
    v = v * (1 / Norm.euclidean_norm(v))
    return create_householder_matrix(v)
