import random

from src.Cryptography.Ciphers.Cipher import Cipher
from src.NumberTheory import utils
from src.NumberTheory.EuclideanAlgorithm import extended_euclidean_algorithm
from src.NumberTheory.PrimeGenerator import PrimeGenerator


class RSA(Cipher):

    def __init__(self, r=None, sk=None, *args, **kwargs):
        if sk is None:
            sk, self.pk = self.create_key(r)
        super().__init__(sk, *args, **kwargs)

    def encrypt(self, message):
        message = self.str2int(message)
        return utils.power(message, self.pk[1], self.pk[0])

    def decrypt(self, ciphertext):
        return self.int2str(utils.power(ciphertext, self.sk[1], self.sk[0]))

    def create_key(self, r, *args, **kwargs):
        l = (r + 2) // 2
        prime_generator = PrimeGenerator.std_insecure()
        p = prime_generator.generate_prime(2 ** l, 2 ** (l + 1) - 1)
        while (q:= prime_generator.generate_prime(2 ** l, 2 ** (l + 1) - 1)) == p:
            pass
        n = q * p
        phin = (q - 1) * (p - 1)
        while extended_euclidean_algorithm(e := random.randint(2, phin), phin)[0] != 1:
            pass
        return (n, e), (n, utils.get_inverse_element(e, phin))




def RSATest():

    ms = 'NSA aus USA hasst RSA.'
    m = ms
    print("Klartext als String:      " + ms)
    r = 1024#len() - 2  # Laenge des Klartexts bestimmen
    rsa = RSA(r)
    c = rsa.encrypt(m)
    print("Chiffretext als Zahl:     " + str(c))
    b = rsa.decrypt(c)
    print("entschl. Text als String: " + b)
    return


RSATest()
