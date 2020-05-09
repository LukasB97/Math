from abc import ABC, abstractmethod
from typing import Set

from src.Algebra.Structures.Function.Interfaces.Evaluable import Evaluable


class Function(Evaluable, ABC):

    @abstractmethod
    def get_variable_context(self) -> Set[str]:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __radd__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __rsub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def __rtruediv__(self, other):
        pass

    @abstractmethod
    def __pow__(self, other):
        pass

    @abstractmethod
    def __rpow__(self, other):
        pass



