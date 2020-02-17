from Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from Algebra.Structures.Matrix.Vector import Vector
from Core.Factories.MatrixFactory import MatrixFactory


def scalar_product(v, u):
    return sum(v[i] * u[i] for i in range(len(v)))


def create_orthogonal_vector(*vectors: Vector):
    matrix = MatrixFactory.matrix_of_column_vectors(*vectors)
    qr_decomposition = QRDecomposition()
    return qr_decomposition.solve(matrix.transpose(), 0)
