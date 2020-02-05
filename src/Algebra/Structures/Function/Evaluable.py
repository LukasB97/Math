from abc import ABC, abstractmethod
from collections import Sized

from Algebra.Structures.Function.VariableContext import VariableContext


class Evaluable(ABC, Sized, VariableContext):

    @abstractmethod
    def evaluate(self, *args, **kwargs) -> float:
        pass

    def __call__(self, *args, **kwargs):
        return self.evaluate(*args, **kwargs)
