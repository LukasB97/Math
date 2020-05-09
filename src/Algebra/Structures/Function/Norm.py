from typing import Set

from src.Algebra.Structures.Function.Interfaces.Function import Function


class Norm(Function):

    def get_variable_context(self) -> Set[str]:
        pass

    def evaluate(self, *args, **kwargs) -> float:
        pass

    @staticmethod
    def euclidean_norm(v):
        s = 0
        for i in range(v.row_count):
            s += v[i, 0] ** 2
        return s ** 0.5
