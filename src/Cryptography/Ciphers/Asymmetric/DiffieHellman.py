import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Constants import GEN,MOD
from src.NumberTheory import utils
from src.NumberTheory.utils import power


class DiffieHellman(AsymmetricCipher):

    def create_key(self, key_length=256, *args, **kwargs):
        public_key = self.create_public_key(key_length, *args, **kwargs)
        secret_key = self.rng.generate_random_integer(1, public_key[MOD] - 1)
        return secret_key, public_key

    def encrypt(self, message):
        return utils.exp(self.public_key[GEN], self.public_key[MOD], self.secret_key)

    def decrypt(self, other_exp):
        return pow(other_exp, self.secret_key, self.public_key[MOD])

    def create_random_generator(self, mod):
        while True:
            generator = random.randint(2, mod - 1)
            if power(generator, (mod - 1) // 2, mod) != 1:
                break
        return generator

    def create_public_key(self, key_length=256, *args, **kwargs):
        safe_prime = self.rng.generate_safe_prime(bits=key_length)
        generator = self.create_random_generator(safe_prime)
        return {
            GEN: generator,
            MOD: safe_prime
        }


    def get_secret_key(self, other_exp):
        return pow(other_exp, self.secret_key, self.public_key[MOD])
