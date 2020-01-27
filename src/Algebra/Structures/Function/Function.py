from typing import List, Set

from src.Algebra.Structures.Function.AbstractFunction import AbstractFunction
from src.Algebra.Structures.Function.Evaluable import Evaluable


class Function(AbstractFunction):

    def get_derivative(self, variable):
        if variable in self.context:
            return self

    def get_anti_derivative(self, variable):
        pass

    def get_variable_context(self) -> Set[str]:
        context = set()
        for op in self.operands:
            if isinstance(op, Evaluable):
                context.update(op.get_variable_context())
        return context

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
