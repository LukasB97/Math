from abc import abstractmethod
from typing import Set

from src.Algebra.Structures.Function.Derivable import Derivable
from src.Algebra.Structures.Function.Evaluable import Evaluable
from src.Algebra.Structures.Function.Operation.Add import Add
from src.Algebra.Structures.Function.Operation.Div import Div
from src.Algebra.Structures.Function.Operation.Mul import Mul
from src.Algebra.Structures.Function.Operation.Pow import Pow
from src.Algebra.Structures.Function.Operation.Sub import Sub


class AbstractFunction(Evaluable, Derivable):

    def __init__(self, operation: Evaluable):
        self.root_operation = operation

    @abstractmethod
    def get_variable_context(self) -> Set[str]:
        pass

    def __mul__(self, other):
        return type(self)(Mul(self, other))

    def __add__(self, other):
        return type(self)(Add(self, other))

    def __truediv__(self, other):
        return type(self)(Div(self, other))

    def __pow__(self, power, modulo=None):
        return type(self)(Pow(self, power))

    def __sub__(self, other):
        return type(self)(Sub(self, other))

    def __rmul__(self, other):
        return type(self)(Mul(other, self))

    def __radd__(self, other):
        return type(self)(Add(other, self))

    def __rtruediv__(self, other):
        return type(self)(Div(other, self))

    def __rpow__(self, power, modulo=None):
        return type(self)(Pow(power, self))

    def __rsub__(self, other):
        type(self)(Sub(other, self))
