from src.NumberTheory.EuclideanAlgorithm import extended_euclidean_algorithm


def square_multiply():
    pass

def get_inverse_element(e, n):  # Inverses mod n
    # Aufruf: ModInv(e,n) mit natuerlichen Zahlen e,n>0 und ggT(e,n)=1
    # Ausgabe: d aus {1,...,n-1} mit (d*e)%n = 1
    return extended_euclidean_algorithm(e, n)[1]


def power(g_base, a, p_mod):
    x = 1
    bits = "{0:b}".format(a)
    for i, bit in enumerate(bits):
        if bit == '1':
            x = (((x ** 2) * g_base) % p_mod)
        elif bit == '0':
            x = ((x ** 2) % p_mod)
    return x % p_mod