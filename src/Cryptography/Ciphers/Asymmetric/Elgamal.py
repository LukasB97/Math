import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Constants import MOD, GEN, PUB, PRIV
from src.NumberTheory.utils import power


class Elgamal(AsymmetricCipher):



    def encrypt_bytes(self, bytes_to_encrypt: bytes, recipient_public_key, **kwargs) -> bytes:
        data = int.from_bytes(bytes_to_encrypt)
        rand_exp = self.rng.generate_random_integer(0, self.secret_key[MOD] - 1)
        rand_element = self.secret_key[GEN] ** rand_exp
        c1 = recipient_public_key[PUB] ** rand_exp * dat


    def decrypt_bytes(self, bytes_to_decrypt: bytes) -> bytes:
        pass

    def create_random_generator(self, mod):
        while True:
            generator = random.randint(2, mod - 1)
            if power(generator, (mod - 1) // 2, mod) != 1:
                break
        return generator

    def create_key(self, key_length, *args, **kwargs):
        mod = self.rng.generate_safe_prime(bits=key_length)
        generator = self.create_random_generator(mod)
        secret = random.randint(0, mod - 2)
        public_secret = power(generator, secret, mod)
        return {MOD: mod, GEN: generator, PRIV: secret}, {MOD: mod, GEN: generator, PUB: public_secret}

    def create_public_key(self):
        return {
            MOD: self.secret_key[MOD],
            GEN: self.secret_key[GEN],
            PUB: power(self.secret_key[GEN], self.secret_key[PRIV], self.secret_key[MOD])
        }
