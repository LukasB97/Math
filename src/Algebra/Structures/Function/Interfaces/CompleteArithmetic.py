from abc import abstractmethod

from Algebra.Structures.Function.Interfaces.Arithmetic import Arithmetic


class CompleteArithmetic(Arithmetic):

    @abstractmethod
    def __rmul__(self, other):
        pass

    @abstractmethod
    def __radd__(self, other):
        pass

    @abstractmethod
    def __rtruediv__(self, other):
        pass

    @abstractmethod
    def __rpow__(self, power, modulo=None):
        pass

    @abstractmethod
    def __rsub__(self, other):
        pass
