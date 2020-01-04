from abc import ABC, abstractmethod

from src.AlgebraicStructures.Function.Evaluable import Evaluable


class Operator(Evaluable):

    def __init__(self, sign, priority):
        self._sign = sign
        self._priority = priority

    @property
    def priority(self):
        return self._priority

    @property
    def sign(self):
        return self._sign

    def __eq__(self, other):
        return other.sign == self.sign and self.priority == other.priority

    @abstractmethod
    def derive(self, variable, operands: list):
        pass

