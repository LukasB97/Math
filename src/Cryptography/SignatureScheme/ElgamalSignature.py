from src.Cryptography.Ciphers.Asymmetric.Elgamal import Elgamal
from src.Cryptography.Constants import MOD, GEN
from src.Cryptography.SignatureScheme.SignatureAlgorithm import SignatureAlgorithm
from src.NumberTheory.EuclideanAlgorithm import gcd


class ElgamalSignature(SignatureAlgorithm, Elgamal):


    def create_signature(self, message):
        rand_x = self.rng.generate_random_integer(1, self.secret_key[MOD] - 2)
        while gcd(rand_x, self.secret_key[MOD] - 1) != 1:
            rand_x = self.rng.generate_random_integer(1, self.secret_key[MOD] - 2)
        r = pow(self.secret_key[GEN], rand_x, self.secret_key[MOD])
        k =


    def verify_signature(self, message, signature, signed_by_pk=None, *args, **kwargs):
        pass
