from src.Cryptography.Ciphers.Asymmetric.Elgamal import Elgamal
from src.Cryptography.SignatureScheme.SignatureAlgorithm import SignatureAlgorithm


class ElgamalSignature(SignatureAlgorithm, Elgamal):

    def create_signature(self, message):
        pass

    def verify_signature(self, message, signature):
        pass
