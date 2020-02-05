from abc import abstractmethod
from collections import Sized

from src.Algebra.Structures.Function.Derivable import Derivable
from src.Algebra.Structures.Function.Evaluable import Evaluable


class ComputationalGraphPart(Evaluable, Derivable, Sized):
    _sign: str

    def __init__(self, left_op, right_op):
        self.left_op = left_op
        self.right_op = right_op

    @abstractmethod
    def evaluate(self, *args, **kwargs):
        pass

    def derive_ops(self, variable):
        return 1, 1

    def _get_values(self, *args, **kwargs):
        left_op = None
        right_op = None
        if isinstance(self.left_op, Evaluable):
            left_op = self.left_op.evaluate(*args, **kwargs)
        else:
            left_op = self.left_op
        if isinstance(self.right_op, Evaluable):
            right_op = self.right_op.evaluate(*args, **kwargs)
        else:
            right_op = self.right_op
        return left_op, right_op

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

    def __len__(self):
        length = 0
        if isinstance(self.left_op, Sized):
            length += len(self.left_op)
        else:
            length += 1
        if isinstance(self.right_op, Sized):
            length += len(self.right_op)
        else:
            length += 1
        return length
