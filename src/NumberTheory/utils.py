from src.NumberTheory import PrimeNumberTests
from src.NumberTheory.EuclideanAlgorithm import extended_euclidean_algorithm, gcd
from src.Tools.NumberGenerator.AbstractNumberGenerator import NumberGenerator
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator

generator = PrimeGenerator.std_insecure()

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

def legendre_symbol(number_to_test, mod):
    if mod == 2:
        if number_to_test % 2 == 0:
            return True
        return None
    result = pow(number_to_test, (mod - 1) / 2, mod)
    if result == 1:
        return True
    elif result == mod - 1:
        return False
    return None

def exp(y, p, a):
    raise NotImplementedError()


def is_quadratic_residue(x, p, q):  # testet, ob x quadratic Rest mod p*q ist
    # call: IsQuadraticResidue(x,p,q) mit prime numbers p,q und
    #         x aus {1,...,p*q-1} mit ggT(x,p*q)=1
    # return: True, falls es ein a aus {1,...,p*q-1} gibt mit a*a=x (mod p*q)
    #          False, sonst
    # mod = p * q
    # for i in range(mod - 1):
    #     if x % mod == (i ** 2) % mod:
    #         return True
    return pow(x, (p - 1) / 2, p) == pow(x, (q - 1) / 2, q) == 1


def random_mul_group(n):
    gen = NumberGenerator()
    a = gen.generate_random_integer(1, n - 1)
    while gcd(n, a) != 1:
        a = gen.generate_random_integer(1, n - 1)
    return a


def sqrt_of_one_mod(number_to_test, modulo):
    return ((number_to_test ** 2) % modulo) == 1

def ord_in_mod(element_to_test, mod):
    i = 1
    while True:
        if (element_to_test ** i) % mod == 1:
            return i
        i += 1


def group_mod_has_generator(m):
    if m == 2 or m == 4:
        return True
    base_prime = generator.get_next_prime(4)
    while base_prime <= m:
        i = 1
        while (prime := base_prime ** i) <= m:
            if prime == m or 2 * prime == m:
                return True
            i += 1
        base_prime = generator.get_next_prime(4)
    return False

def is_fermat_witness(to_test, witness_for):
    return pow(to_test, witness_for - 1, witness_for) != 1

def is_fermat_liar(to_test, liar_for):
    if PrimeNumberTests.aks(liar_for):
        return False
    return pow(to_test, liar_for - 1, liar_for) == 1

def is_carmichael_number(x):
    """
    An uneven element of N\P is a carmichael number if
    a^(n-1) = 1 mod n for all a element of Zx
    """
    if x % 2 == 0:
        return False
    if PrimeNumberTests.aks(x):
        return False
    for i in range(x):
        if pow(i, x - 1, x) != 1:
            return False
    return True

def get_generator_mod(m):
    pass


def primitive_root_mod(m):
    """
    A number x is a primitive root mod m
    if the order of a under m equals the euler totient function of m
    @param m:
    @return:
    """
    order = euler_phi(m)
    for i in range(1, m):
        if ord_in_mod(i, m) == order:
            return i
    return None


def multiplicative_group_mod(mod):
    elements = set()
    for i in range(1, mod + 1):
        if gcd(i, mod) == 1:
            elements.add(i)
    return elements

def euler_phi(n):
    """
    @param n:
    @return: Order
    """
    pass


