from typing import List

from src.Algebra.Structures.Function.Function import Function


class Polynomial(Function):

    def __init__(self, operator, operands: List[Evaluable], coefficients: List[float] = None):
        super().__init__(operator, operands)
        if coefficients is None:
            coefficients = []
        self.coeffcients = coefficients

