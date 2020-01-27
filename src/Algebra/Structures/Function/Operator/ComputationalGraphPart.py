from abc import abstractmethod

from src.Algebra.Structures.Function.Derivable import Derivable
from src.Algebra.Structures.Function.Evaluable import Evaluable


class ComputationalGraphPart(Evaluable, Derivable):
    _sign: str

    def __init__(self, left_op, right_op):
        self.left_op = left_op
        self.right_op = right_op

    @abstractmethod
    def evaluate(self, first_op, second_op):
        pass

    @property
    def sign(self):
        return self._sign

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.left_op) + " " + self.sign + " " + str(self.right_op)

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self).replace(' ', '') == other.replace(' ', '')
