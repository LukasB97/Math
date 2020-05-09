from typing import Set

from src.Algebra.Structures.Function import TranscendentalFunctionMapping
from src.Algebra.Structures.Function.Interfaces.Function import Function
from src.Algebra.Structures.Function.Parser.ParseException import ParseException


class TranscendentalFunction(Function):

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
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

    def __len__(self) -> int:
        pass

    def __init__(self, representation, function, params):
        super().__init__(function, params)
        self.representation = representation

    def evaluate(self, *args, **kwargs) -> float:
        raise NotImplementedError()

    def get_variable_context(self) -> Set[str]:
        pass

    def get_derivative(self, variable):
        pass

    def get_anti_derivative(self, variable):
        pass

    @classmethod
    def from_string(cls, expression, parameter):
        if expression not in TranscendentalFunctionMapping.mappings:
            raise ParseException("could not find ", expression)
        return TranscendentalFunction(expression, TranscendentalFunctionMapping.mappings[expression], parameter)
