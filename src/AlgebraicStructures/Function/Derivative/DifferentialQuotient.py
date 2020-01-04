from src.AlgebraicStructures.Function.Evaluable import Evaluable


def differential_quotient(f: Evaluable, x):
    h = 1/2**32
    return (f.evaluate(x=x+h)-f.evaluate(x=x))/h