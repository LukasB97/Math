from src.NumberTheory.EuclideanAlgorithm import extended_euclidean_algorithm, greatest_common_divisor
from src.Tools.NumberGenerator.AbstractNumberGenerator import NumberGenerator


def square_multiply():
    pass


def get_inverse_element(e, n):  # Inverses mod n
    # Aufruf: ModInv(e,n) mit natuerlichen Zahlen e,n>0 und ggT(e,n)=1
    # Ausgabe: d aus {1,...,n-1} mit (d*e)%n = 1
    return extended_euclidean_algorithm(e, n)[1]


# def power(g_base, a, p_mod):
#     x = 1
#     bits = "{0:b}".format(a)
#     for i, bit in enumerate(bits):
#         if bit == '1':
#             x = (((x ** 2) * g_base) % p_mod)
#         elif bit == '0':
#             x = ((x ** 2) % p_mod)
#     return x % p_mod


def power(x, y, n):  # Exponentialfunktion mod n
    # Aufruf: ModExp(x,y,n) mit natuerlichen Zahlen x,y,n und n>=2
    # Ausgabe: (x**y)%n
    z = i = 1
    p = x % n
    while i <= y:  # Invariante: p = (x^i)%n
        if i & y > 0:
            z = (z * p) % n
        i = i + i
        p = (p * p) % n
    return z


def IsQuadraticResidue(x, p, q):  # testet, ob x quadratischer Rest mod p*q ist
    # Aufruf: IsQuadraticResidue(x,p,q) mit Primzahlen p,q und
    #         x aus {1,...,p*q-1} mit ggT(x,p*q)=1
    # Ausgabe: True, falls es ein a aus {1,...,p*q-1} gibt mit a*a=x (mod p*q)
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
