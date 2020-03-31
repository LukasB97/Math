import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory.utils import power
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


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
