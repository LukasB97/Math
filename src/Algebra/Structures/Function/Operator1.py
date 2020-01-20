from enum import Enum


def add(values):
    return sum(values)


def sub(values):
    result = values[0]
    for i in range(1, len(values)):
        result -= values[i]
    return result


def mul(values):
    result = 1
    for val in values:
        result *= val
    return result


def pow_Dd(values):
    return values[0] ** values[1]


def div(values):
    return values[0] / values[1]


class Operator(Enum):
    ADD = add
    SUB = sub
    MUL = mul
    DIV = div
    POW = pow_Dd

    @classmethod
    def get(cls, op: str):
        if op == "*":
            return Operator.MUL
        elif op == "/":
            return Operator.DIV
        elif op == "+":
            return Operator.ADD
        elif op == "-":
            return Operator.SUB
        elif op == "^":
            return Operator.POW
        raise ValueError()
