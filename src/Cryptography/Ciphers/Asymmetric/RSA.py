import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory import utils
from src.NumberTheory.EuclideanAlgorithm import greatest_common_divisor
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class RSA(AsymmetricCipher):

    # @property
    # def public_key(self):
    #     pass

    def __init__(self, key_length=None, secret_key=None, pk=None, *args, **kwargs):
        if not ((key_length is None) ^ (secret_key is pk is None)):
            raise ValueError()
        super().__init__(secret_key, pk, *args, **kwargs)

    def encrypt(self, message):
        message = self.str2int(message)
        return utils.power(message, self.public_key[1], self.public_key[0])

    def decrypt(self, ciphertext):
        return self.int2str(utils.power(ciphertext, self.secret_key[1], self.secret_key[0]))

    def create_key(self, key_length=256, *args, **kwargs):
        min_bits = (key_length + 2) // 2
        from_ = 2 ** min_bits
        to_ = 2 ** (min_bits + 1) - 1
        prime_generator = PrimeGenerator.std_insecure()
        p = prime_generator.generate_prime(from_, to_)
        q = p
        while q == p:
            q = prime_generator.generate_prime(from_, to_)
        prime_product = q * p
        phin = (q - 1) * (p - 1)
        random_relatively_prime = random.randint(2, phin)
        while greatest_common_divisor(random_relatively_prime, phin) != 1:
            random_relatively_prime = random.randint(2, phin)
        return (prime_product, random_relatively_prime), (
            prime_product, utils.inverse_mod_n(random_relatively_prime, phin))
