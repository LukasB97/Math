from typing import List

from src.AlgebraicStructures.Function.Evaluable import Evaluable


class AbstractFunction(Evaluable):

    def derive(self, variable) -> 'AbstractFunction':
        return self.operator.derive(self.operands)

    def evaluate(self, *args, **kwargs) -> float:
        values = list()
        for op in self.operands:
            if isinstance(op, Evaluable):
                values.append(op.evaluate(*args, **kwargs))
            else:
                values.append(op)
        return self.operator(values)

    def __init__(self, operator, operands: List[Evaluable]):
        self.operator = operator
        self.operands = operands
