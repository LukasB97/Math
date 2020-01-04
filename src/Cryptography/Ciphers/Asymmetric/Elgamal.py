import random

from src.NumberTheory.PrimeGenerator import PrimeGenerator


def power(g_base, a, p_mod):
    x = 1
    bits = "{0:b}".format(a)
    for i, bit in enumerate(bits):
        if bit == '1':
            x = (((x ** 2) * g_base) % p_mod)
        elif bit == '0':
            x = ((x ** 2) % p_mod)
    return x % p_mod


def ElgamalKeyGen(l=256):
    # Aufruf: ElgamalKeyGen(l) mit natuerlicher Zahl l>=4
    # Ausgabe: ((p,g,B),(p,g,b)) mit
    #     p = zufaellige l-Bit Primzahl, sodass (p-1)/2 prim ist
    #     g = zufaelliger Erzeuger mod p, d.h. {g**i | 0<i<p} = {1,...,p-1}
    #     b = zufaelliges Element aus {0,...,p-2}
    #     B = (g**b)%p
    prime_generator = PrimeGenerator.std_insecure()
    p = prime_generator.generate_safe_prime(2 ** l, 2 ** (l + 1) - 1)
    g = 0
    while True:
        g = random.randint(2, p - 1)
        if power(g, (p - 1) // 2, p) != 1:
            break
    b = random.randint(0, p - 2)
    B = power(g, b, p)
    return (p, g, B), (p, g, b)


def ElgamalEncrypt(pk, m):
    # Aufruf: ElgamalEncrypt(pk,m) mit public key pk und Klartext m
    # Ausgabe: Chiffretext c
    a = random.randint(1, pk[0] - 1)
    A = power(pk[1], a, pk[0])
    c = power(pk[2], a, pk[0])
    c = (c * m) % pk[0]
    return c, A


def ElgamalDecrypt(sk, c, A):
    # Aufruf: ElgamalDecrypt(sk,c) mit secure key sk und Chiffretext c
    # Ausgabe: dechiffrierte Nachricht
    x = sk[0] - 1 - sk[2]
    m = power(A, x, sk[0])
    return (m * c) % sk[0]


def int2str(x):  # codiert Zahl als String
    # Aufruf: int2str(23268733837745479405720608239248647353390)
    # Ausgabe: 'Das ist ein Test.'
    s = ''
    while x > 0:
        s = chr(x & 255) + s
        x = x >> 8
    return s


def str2int(s):  # codiert String als Zahl
    # Aufruf: str2int('Das ist ein Test.')
    # Ausgabe: 23268733837745479405720608239248647353390
    x = 0
    for i in range(0, len(s)):
        x = (x << 8) + ord(s[i])
    return x


def ElgamalTest():
    ms = 'Geheimnis'
    m = str2int(ms)
    print("Klartext als String:           " + ms)
    print("Klartext als Zahl:             " + str(m))
    (pk, sk) = ElgamalKeyGen(90)
    print("Public Key:                    " + str(pk))
    print("Private Key:                   " + str(sk))
    c1, A1 = ElgamalEncrypt(pk, m)
    c2, A2 = ElgamalEncrypt(pk, m)
    print("1. Chiffretext:                " + str(c1))
    print("2. Chiffretext:                " + str(c2))
    b1 = ElgamalDecrypt(sk, c1, A1)
    b2 = ElgamalDecrypt(sk, c2, A2)
    print("1. Chiffretext entschluesselt: " + str(b1))
    print("2. Chiffretext entschluesselt: " + str(b2))
    b1s = int2str(b1)
    b2s = int2str(b2)
    print("1. Chiffretext entschluesselt: " + b1s)
    print("2. Chiffretext entschluesselt: " + b2s)
    return


ElgamalTest()
