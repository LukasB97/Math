from abc import abstractmethod
from collections import Sized
from typing import List

from src.Algebra.Structures.Function.Interfaces.Evaluable import Evaluable


class ComputationalGraphPart(Evaluable, Sized):

    def __init__(self, operands: List, sign: str):
        self.operands = operands
        self.sign = sign

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (" " + self.sign + " ").join(self.operands)

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self).replace(' ', '') == other.replace(' ', '')

    def __len__(self):
        return len(self.operands)

    @abstractmethod
    def evaluate(self, *args, **kwargs):
        pass

    def add_operand(self, op: Evaluable):
        raise NotImplementedError()

    def __mul__(self, other: Evaluable):
        return Mul(self, other)

    def __truediv__(self, other: Evaluable):
        return Div(self, other)

    def __pow__(self, other: Evaluable):
        return Pow(self, other)

    def __add__(self, other: Evaluable):
        return Add(self, other)

    def __sub__(self, other: Evaluable):
        return Sub(self, other)

    def __rmul__(self, other: Evaluable):
        return Mul(other, self)

    def __rtruediv__(self, other: Evaluable):
        return Div(other, self)

    def __rpow__(self, other: Evaluable):
        return Pow(other, self)

    def __radd__(self, other: Evaluable):
        return Add(other, self)

    def __rsub__(self, other: Evaluable):
        return Sub(other, self)


class Add(ComputationalGraphPart):
    _sign = "+"

    def __init__(self, *args):
        operands = list()
        if len(args) != 1:
            operands += args
        else:
            operands += args[0]
        super().__init__(operands, self._sign)

    def add_operand(self, op: Evaluable):
        self.operands.append(op)

    def evaluate(self, *args, **kwargs) -> float:
        result = 0
        for op in self.operands:
            if isinstance(op, Evaluable):
                result += op(*args, **kwargs)
            else:
                result += op
        return result


class Div(ComputationalGraphPart):
    _sign = "/"

    def __init__(self, to_divide: Evaluable, divide_by: Evaluable):
        super().__init__([to_divide, divide_by], self._sign)

    def add_operand(self, op: Evaluable):
        raise NotImplementedError()

    def evaluate(self, *args, **kwargs) -> float:
        if isinstance(self.operands[0], Evaluable):
            to_div = self.operands[0](*args, **kwargs)
        else:
            to_div = self.operands[0]
        if isinstance(self.operands[1], Evaluable):
            return to_div / self.operands[1](*args, **kwargs)
        else:
            return to_div / self.operands[1]


class Mul(ComputationalGraphPart):
    _sign = "*"

    def __init__(self, *args):
        operands = list()
        if len(args) != 1:
            operands += args
        else:
            operands += args[0]
        super().__init__(operands, self._sign)

    def add_operand(self, op: Evaluable):
        self.operands.append(op)

    def evaluate(self, *args, **kwargs) -> float:
        result = 1
        for op in self.operands:
            if isinstance(op, Evaluable):
                result *= op(*args, **kwargs)
            else:
                result *= op
        return result


class Pow(ComputationalGraphPart):
    _sign = "^"

    def __init__(self, *args):
        operands = list()
        if len(args) != 1:
            operands += args
        else:
            operands += args[0]
        super().__init__(operands, self._sign)

    def add_operand(self, op: Evaluable):
        raise NotImplementedError()

    def evaluate(self, *args, **kwargs) -> float:
        if isinstance(self.operands[0], Evaluable):
            base = self.operands[0](*args, **kwargs)
        else:
            base = self.operands[0]
        if isinstance(self.operands[1], Evaluable):
            return base ** self.operands[1](*args, **kwargs)
        else:
            return base ** self.operands[1]


class Sub(ComputationalGraphPart):
    _sign = "-"

    def __init__(self, *args):
        operands = list()
        if len(args) != 1:
            operands += args
        else:
            operands += args[0]
        super().__init__(operands, self._sign)

    def add_operand(self, op: Evaluable):
        self.operands.append(op)

    def evaluate(self, *args, **kwargs) -> float:
        if isinstance(self.operands[0], Evaluable):
            result = self.operands[0]()
        else:
            result = self.operands[0]
        for op in self.operands[1:]:
            if isinstance(op, Evaluable):
                result -= op(*args, **kwargs)
            else:
                result -= op
        return result
