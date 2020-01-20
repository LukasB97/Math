from typing import List, Set

from src.Algebra.Structures.Function.Evaluable import Evaluable
from src.Algebra.Structures.Function.Operator1 import Operator


class Function(Evaluable):

    def get_variable_context(self) -> Set[str]:
        context = set()
        for op in self.operands:
            if isinstance(op, Evaluable):
                context.update(op.get_variable_context())
        return context

    def derive(self, variable) -> 'Function':
        return self.operator.derive(self.operands)

    def __mul__(self, other):
        return Function(Operator.MUL, [self, other])

    def __add__(self, other):
        return Function(Operator.ADD, [self, other])

    def __truediv__(self, other):
        return Function(Operator.DIV, [self, other])

    def __pow__(self, power, modulo=None):
        return Function(Operator.POW, [self, power])

    def __sub__(self, other):
        return Function(Operator.SUB, [self, other])

    def __rmul__(self, other):
        return Function(Operator.MUL, [self, other])

    def __radd__(self, other):
        return Function(Operator.ADD, [self, other])

    def __rtruediv__(self, other):
        return Function(Operator.DIV, [other, self])

    def __rpow__(self, power, modulo=None):
        return Function(Operator.POW, [power, self])

    def __rsub__(self, other):
        return Function(Operator.SUB, [other, self])

    def evaluate(self, *args, **kwargs) -> float:
        if len(kwargs) != 0:
            if len(self.context) != len(kwargs):
                raise ValueError("parameter error")
        elif len(args) != len(self.context):
            raise ValueError("parameter error")
        elif len(args) == 1:
            kwargs = {
                list(self.context)[0]: args[0]
            }
        else:
            raise ValueError("parameter error")
        values = list()
        for op in self.operands:
            if isinstance(op, Evaluable):
                values.append(op.evaluate(*args, **kwargs))
            else:
                values.append(op)
        return self.operator(values)

    def __call__(self, *args, **kwargs):
        return self.evaluate(*args, **kwargs)

    def __init__(self, operator, operands: List[Evaluable]):
        self.operator = operator
        self.operands = operands
        self.context = self.get_variable_context()
