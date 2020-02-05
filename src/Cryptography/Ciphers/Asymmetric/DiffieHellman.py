import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory.PrimeNumberTests import miller_rabin_test
from src.NumberTheory.utils import power


class DiffieHellman(AsymmetricCipher):

    def get_public_key(self):
        pass

    def encrypt(self, message):
        pass

    def decrypt(self, chiffretext):
        pass

    def create_key(self, l, *args, **kwargs):
        p = 10
        g = 0
        i = 0
        lower = 2 ** l
        upper = (2 ** (l + 1)) - 1
        while not miller_rabin_test(p) or not miller_rabin_test((p - 1) // 2):
            p = random.randint(lower, upper)
        while True:
            g = random.randint(2, p - 1)
            if power(g, (p - 1) // 2, p) != 1:
                break
        return g, p


def DHTest():  # Diffie-Hellman-Test
    (g, p) = DiffieHellman()
    pk1 = power(g, 14, p)
    pk2 = power(g, 22, p)
    return power(pk1, 22, p)


DHTest()
