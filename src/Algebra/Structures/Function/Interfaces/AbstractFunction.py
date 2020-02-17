from abc import abstractmethod
from typing import Set

from Algebra.Structures.Function.Interfaces.Arithmetic import Arithmetic
from Algebra.Structures.Function.Interfaces.Evaluable import Evaluable
from Algebra.Structures.Function.Interfaces.VariableContext import VariableContext


class AbstractFunction(Evaluable, VariableContext, Arithmetic):

    def __init__(self, operation: Evaluable):
        self.root_operation = operation

    @abstractmethod
    def get_variable_context(self) -> Set[str]:
        pass

