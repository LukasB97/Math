import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory.PrimeGenerator import PrimeGenerator
from src.NumberTheory.utils import power


class Elgamal(AsymmetricCipher):

    def get_public_key(self):
        pass

    def encrypt(self, message):
        a = random.randint(1, self.pk[0] - 1)
        A = power(self.pk[1], a, self.pk[0])
        c = power(self.pk[2], a, self.pk[0])
        c = (c * message) % self.pk[0]
        return c, A

    def decrypt(self, chiffretext, A):
        x = self.sk[0] - 1 - self.sk[2]
        m = power(A, x, self.sk[0])
        return (m * chiffretext) % self.sk[0]

    def create_key(self, *args, **kwargs):
        l = kwargs["l"]
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
