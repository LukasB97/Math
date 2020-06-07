import string
import unittest
from random import choices

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Ciphers.Asymmetric.DiffieHellman import DiffieHellman
from src.Cryptography.Ciphers.Asymmetric.Elgamal import Elgamal
from src.Cryptography.Ciphers.Asymmetric.RSA import RSA
from src.Cryptography.Ciphers.Cipher import Cipher
from src.Cryptography.Ciphers.Symmetric.AES import AES
from src.Cryptography.SignatureScheme.RSASignature import RSASignature
from src.Cryptography.SignatureScheme.SignatureAlgorithm import SignatureAlgorithm


class SignatureTests(unittest.TestCase):

    @staticmethod
    def create_random_string(n=32):
        return ''.join(choices(string.ascii_uppercase + string.digits, k=n))

    def _test_single(self, text, sig1: SignatureAlgorithm, sig2: SignatureAlgorithm):
        signature1 = sig1.create_signature(text)
        signature2 = sig2.create_signature(text)
        self.assertFalse(sig1.verify_signature(text, signature2))
        self.assertFalse(sig2.verify_signature(text, signature1))
        self.assertTrue(sig1.verify_signature(text, signature2, sig2.public_key))
        self.assertTrue(sig2.verify_signature(text, signature1, sig1.public_key))

    def _test_single_scheme(self, sig, iterations=10):
        for i in range(iterations):
            self._test_single(self.create_random_string(), sig(), sig())

    def test_rsa_sig(self):
        self._test_single_scheme(RSASignature)




if __name__ == '__main__':
    unittest.main()
