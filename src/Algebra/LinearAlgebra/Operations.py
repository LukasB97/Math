from Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from Algebra.Structures.Function.Norm import Norm
from Algebra.Structures.Matrix.Vector import Vector
from Core.Lina.MatrixFactory import MatrixFactory
from Core.Lina.VectorFactory import VectorFactory


def scalar_product(v, u):
    return sum(v[i] * u[i] for i in range(len(v)))


def create_orthonormal_vector(*vectors: Vector):
    missing_column_vectors = vectors[0].row_count - len(vectors)
    null_vectors = []
    for i in range(missing_column_vectors):
        null_vectors.append(VectorFactory.null_vector(vectors[0].row_count))
    matrix = MatrixFactory.matrix_of_column_vectors(*vectors, *null_vectors)
    qr_decomposition = QRDecomposition()
    created_vector = qr_decomposition.solve(matrix.transpose(), 0)
    return created_vector * (1 / Norm.euclidean_norm(created_vector))

