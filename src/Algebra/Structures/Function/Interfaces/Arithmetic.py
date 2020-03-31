from abc import ABC, abstractmethod


class Arithmetic(ABC):

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass

    @abstractmethod
    def __pow__(self, power, modulo=None):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass
