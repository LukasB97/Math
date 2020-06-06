import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory.utils import power
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class Elgamal(AsymmetricCipher):

    def get_public_key(self):
        pass

    def encrypt(self, message):
        a = random.randint(1, self.public_key[0] - 1)
        kp = power(self.public_key[1], a, self.public_key[0])
        c = power(self.public_key[2], a, self.public_key[0])
        c = (c * message) % self.public_key[0]
        return c, kp

    def decrypt(self, chiffretext, a):
        x = self.secret_key[0] - 1 - self.secret_key[2]
        m = power(a, x, self.secret_key[0])
        return (m * chiffretext) % self.secret_key[0]

    def create_key(self, key_length, *args, **kwargs):
        p = self.rng.generate_safe_prime(2 ** key_length, 2 ** (key_length + 1) - 1)
        while True:
            g = random.randint(2, p - 1)
            if power(g, (p - 1) // 2, p) != 1:
                break
        b = random.randint(0, p - 2)
        kp = power(g, b, p)
        return (p, g, kp), (p, g, b)
