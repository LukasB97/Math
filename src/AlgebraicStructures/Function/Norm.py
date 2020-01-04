from src.AlgebraicStructures.Function.AbstractFunction import AbstractFunction


class Norm(AbstractFunction):

    def euclidean_norm(v):
        s = 0
        for i in range(v.row_count):
            s += v[i, 0] ** 2
        return s ** 0.5
