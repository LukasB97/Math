from src.Algebra.Structures.Function.Function import Function


class Norm(Function):

    @staticmethod
    def euclidean_norm(v):
        s = 0
        for i in range(v.row_count):
            s += v[i, 0] ** 2
        return s ** 0.5
