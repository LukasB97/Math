from src.Algebra.Structures.Function import Evaluable


def differential_quotient(f: Evaluable, x):
    h = 1 / 2 ** 32
    return (f(x + h) - f(x)) / h
