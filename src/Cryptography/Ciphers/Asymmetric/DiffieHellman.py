import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory.utils import power
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class DiffieHellman(AsymmetricCipher):

    def public_key(self):
        pass

    def encrypt(self, message):
        pass

    def decrypt(self, chiffretext):
        pass

    def create_key(self, key_length=256, prime_generator=PrimeGenerator.std_insecure(), *args, **kwargs):
        lower = 2 ** key_length
        upper = (2 ** (key_length + 1)) - 1
        safe_prime = prime_generator.generate_safe_prime(lower, upper)
        while True:
            g = random.randint(2, safe_prime - 1)
            if power(g, (safe_prime - 1) // 2, safe_prime) != 1:
                break
        return g, safe_prime
