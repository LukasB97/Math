from typing import List, Set

from Algebra.Structures.Function.Interfaces.AbstractFunction import AbstractFunction
from Algebra.Structures.Function.Interfaces.Derivable import Derivable
from Algebra.Structures.Function.Interfaces.ElementaryAntiDerivative import ElementaryAntiDerivative


class Polynomial(AbstractFunction, Derivable, ElementaryAntiDerivative):

    def get_variable_context(self) -> Set[str]:
        return set(self.variable_name)

    def evaluate(self, *args, **kwargs) -> float:
        if len(args) == 1:
            m = args[1]
        else:
            m = kwargs[self.variable_name]
        res = 0
        for i in range(len(self)):
            res += self.coefficients[i] * m ** i
        return res

    def get_derivative(self, variable: str):
        new_coefficients = []
        for i in range(1, len(self)):
            new_coefficients.append(self.get_coefficient(i) * i)
        return Polynomial(new_coefficients)

    def get_anti_derivative(self, variable):
        new_coefficients = [0]
        for i in range(len(self)):
            new_coefficients.append(self.get_coefficient(i) / (i + 1))
        return Polynomial(new_coefficients)

    def get_coefficient(self, i):
        if len(self) > i:
            return self.coefficients[i]
        return 0

    def __len__(self):
        return len(self.coefficients)

    def __init__(self, coefficients: List[float] = None, variable_name="x"):
        self.variable_name = variable_name
        if coefficients is None:
            coefficients = []
        self.coefficients = coefficients

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if len(self) >= len(other):
                coefficients = self.coefficients.copy()
                for i in range(len(other)):
                    coefficients[i] += other.coefficients[i]
            else:
                coefficients = other.coefficients.copy()
                for i in range(len(self)):
                    coefficients[i] += self.coefficients[i]
            return Polynomial(coefficients)
        raise NotImplementedError()

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            if len(self) >= len(other):
                coefficients = self.coefficients.copy()
                for i in range(len(other)):
                    coefficients[i] -= other.coefficients[i]
            else:
                coefficients = other.coefficients.copy()
                for i in range(len(self)):
                    coefficients[i] -= self.coefficients[i]
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
