from src.AlgebraicStructures.Function.Derivative import DifferentialQuotient


def start(f, x, i):
    x_n = x
    for j in range(i):
        x_n = x_n - f.evaluate(x=x_n)/DifferentialQuotient.differential_quotient(f, x_n)
    return x_n

