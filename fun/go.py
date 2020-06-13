from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Core.Lina import Decompositions

from tests.MathTests.AlgebraTests.MatrixTests.Matrices import complex_4x4_1

m = Matrix([
    [1, -2, 1],
    [1, 1, -1],
    [1, 4, 2]
])
decomp = Decompositions.lr_decomposition
decomp.decompose(m)
print(decomp.decompose(m))
print(m * Matrix([
    [2],
    [-1],
    [-1]
]))
print(m * Matrix([
    [-1],
    [2],
    [-1]
]))
print(m * Matrix([
    [-2],
    [0],
    [2]
]))
print(decomp.decompose(Matrix([
    [3, -6, 0],
    [2, 2, -4],
    [-4, 5, 2]
])))