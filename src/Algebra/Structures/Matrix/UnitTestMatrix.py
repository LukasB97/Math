from src.Algebra.Structures.Matrix.Matrix import Matrix


class UnitTestMatrix(Matrix):

    def __init__(self, matrix_vectors, round_digits=None, *args, **kwargs):
        if round_digits is not None:
            self.delta = 10 ** (-round_digits)
        else:
            self.delta = 0
        super().__init__(matrix_vectors=matrix_vectors, *args, **kwargs)

    def value_equality(self, a, b) -> bool:
        return abs(a - b) <= self.delta
