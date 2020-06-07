from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Core.Lina import Decompositions

from tests.MathTests.AlgebraTests.MatrixTests.Matrices import complex_4x4_1

m = Matrix(complex_4x4_1, dtype=complex)
decomp = Decompositions.lr_decomposition
decomp.decompose(m)
print(decomp.decompose(m))