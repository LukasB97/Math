from src.NumberTheory.EuclideanAlgorithm import extended_euclidean_algorithm, greatest_common_divisor
from src.Tools.NumberGenerator.AbstractNumberGenerator import NumberGenerator


def inverse_mod_n(e, n):  # Inverses mod n
    # call: ModInv(e,n) mit natural numbers e,n>0 und ggT(e,n)=1
    # return: d aus {1,...,n-1} mit (d*e)%n = 1
    return extended_euclidean_algorithm(e, n)[1]


def power(x, y, n):  # Exponentialfunktion mod n
    # call: ModExp(x,y,n) mit natural numbers x,y,n und n>=2
    # return: (x**y)%n
    z = i = 1
    p = x % n
    while i <= y:  # Invariante: p = (x^i)%n
        if i & y > 0:
            z = (z * p) % n
        i = i + i
        p = (p * p) % n
    return z


def is_quadratic_residue(x, p, q):  # testet, ob x quadratic Rest mod p*q ist
    # call: IsQuadraticResidue(x,p,q) mit prime numbers p,q und
    #         x aus {1,...,p*q-1} mit ggT(x,p*q)=1
    # return: True, falls es ein a aus {1,...,p*q-1} gibt mit a*a=x (mod p*q)
    #          False, sonst
    mod = p * q
    for i in range(mod - 1):
        if x % mod == (i ** 2) % mod:
            return True
    return False


def random_mul_group(n):
    gen = NumberGenerator()
    a = gen.generate_random_integer(1, n - 1)
    while greatest_common_divisor(n, a) != 1:
        a = gen.generate_random_integer(1, n - 1)
    return a
