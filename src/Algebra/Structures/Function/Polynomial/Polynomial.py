from typing import List, Set

from src.Algebra.Structures.Function.Interfaces.Function import Function


class Polynomial(Function):

    def __init__(self, coefficients: List[float] = None):
        if coefficients is None:
            coefficients = []
        self.coefficients = coefficients

    def __getitem__(self, item):
        return self.coefficients[item]

    def __len__(self):
        return len(self.coefficients)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if len(self) >= len(other):
                coefficients = self.coefficients.copy()
                for i in range(len(other) - 1, -1, -1):
                    coefficients[i] += other.coefficients[i]
            else:
                coefficients = other.coefficients.copy()
                for i in range(len(self) - 1, -1, -1):
                    coefficients[i] += self.coefficients[i]
            return Polynomial(coefficients)
        raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            coefficients = self.coefficients.copy()
            for i in range(max(len(self), len(other))):
                if len(coefficients) > i and len(other) > i:
                    coefficients[i] -= other.coefficients[i]
                elif len(other) > i:
                    coefficients.append(-other[i])
            return Polynomial(coefficients)
        raise NotImplementedError()

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            coefficients = []
            for i in range(len(self) * len(other)):
                ith_coefficient = 0
                for k in range(i + 1):
                    ith_coefficient += self.get_coefficient(i - k) * other.get_coefficient(k)
                coefficients.append(ith_coefficient)
            return Polynomial(coefficients)
        raise NotImplementedError()

    @property
    def degree(self) -> int:
        return len(self) - 1

    def get_variable_context(self) -> Set[str]:
        return set("x")

    def evaluate(self, x, *args, **kwargs) -> float:
        result = self.coefficients[-1]
        for i in range(len(self)-2, -1, -1):
            result *= x
            result += self.coefficients[i]
        return result

    def get_derivative(self, variable: str):
        # new_coefficients = []
        # for i in range(1, len(self)):
        #     new_coefficients.append(self.get_coefficient(i) * i)
        # return Polynomial(new_coefficients)
        pass

    def get_anti_derivative(self, variable):
        # new_coefficients = [0]
        # for i in range(len(self)):
        #     new_coefficients.append(self.get_coefficient(i) / (i + 1))
        # return Polynomial(new_coefficients)
        pass

    def __radd__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __pow__(self, other):
        pass

    def __rpow__(self, other):
        pass

    def get_coefficient(self, i):
        if len(self) > i:
            return self.coefficients[i]
        return 0
