import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Constants import PRIV, MOD
from src.NumberTheory import utils
from src.NumberTheory.EuclideanAlgorithm import gcd

EXP = "encryption_exponent"


class RSA(AsymmetricCipher):

    def __init__(self, key_length=1024, secret_key=None, *args, **kwargs):
        super().__init__(secret_key=secret_key, key_length=key_length, *args, **kwargs)

    def create_public_key(self):
        return {MOD: self.secret_key[MOD], EXP: 0}

    def encrypt_bytes(self, bytes_to_encrypt: bytes, public_key=None, **kwargs) -> bytes:
        to_encrypt = int.from_bytes(bytes_to_encrypt, "big")
        encrypted = pow(to_encrypt, public_key[EXP], public_key[MOD])
        return encrypted.to_bytes(length=(encrypted.bit_length() + 7) // 8, byteorder="big")

    def decrypt_bytes(self, bytes_to_decrypt: bytes, **kwargs) -> bytes:
        to_decrypt = int.from_bytes(bytes_to_decrypt, "big")
        decrypted = pow(to_decrypt, self.secret_key[PRIV], self.secret_key[MOD])
        res = decrypted.to_bytes(length=(decrypted.bit_length() + 7) // 8, byteorder="big")
        return res

    def create_key(self, key_length=256, *args, **kwargs):
        min_bits = (key_length + 2) // 2
        p = self.rng.generate_prime(bits=min_bits)
        q = self.rng.generate_prime(bits=min_bits)
        while q == p:
            q = self.rng.generate_prime(bits=min_bits)
        prime_product = q * p
        group_order = (q - 1) * (p - 1)
        encryption_exp = self.rng.generate_random_integer(2, group_order - 1)
        while gcd(encryption_exp, group_order) != 1:
            encryption_exp = random.randint(2, group_order)
        secret = utils.inverse_mod_n(encryption_exp, group_order)
        return {MOD: prime_product, PRIV: secret}, {MOD: prime_product, EXP: encryption_exp}
