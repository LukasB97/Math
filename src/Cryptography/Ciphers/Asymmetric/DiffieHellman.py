import random


def power(g_base, a, p_mod):
    x = 1
    bits = "{0:b}".format(a)
    for i, bit in enumerate(bits):
        if bit == '1':
            x = (((x ** 2) * g_base) % p_mod)
        elif bit == '0':
            x = ((x ** 2) % p_mod)
    return x % p_mod


def DHChooseGenerator(l=256):  # Erzeugerwahl fuer Diffie-Hellman
    # Aufruf: DHChooseGenerator(l) mit natuerlicher Zahl l>=4
    # Ausgabe: (g,p) mit
    #     p = zufaellige l-Bit Primzahl, sodass (p-1)/2 prim ist
    #         (d.h. (p-1)/2 ist eine Sophie-Germain-Primzahl)
    #     g = zufaelliger Erzeuger mod p, d.h. {(g**i)%p | 0<i<p} = {1,...,p-1}
    p = 10
    g = 0
    i = 0
    lower = 2 ** l
    upper = (2 ** (l + 1)) - 1
    while not IsPrime(p) or not IsPrime((p - 1) // 2):
        p = random.randint(lower, upper)
    while True:
        g = random.randint(2, p - 1)
        if power(g, (p - 1) // 2, p) != 1:
            break
    return g, p


def DHTest():  # Diffie-Hellman-Test
    (g, p) = DHChooseGenerator()
    pk1 = power(g, 14, p)
    pk2 = power(g, 22, p)
    return power(pk1, 22, p)


DHTest()
