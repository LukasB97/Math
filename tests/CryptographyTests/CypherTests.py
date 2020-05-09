import string
import unittest
from random import choices

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Ciphers.Asymmetric.DiffieHellman import DiffieHellman
from src.Cryptography.Ciphers.Asymmetric.Elgamal import Elgamal
from src.Cryptography.Ciphers.Asymmetric.Goldwasser import Goldwasser
from src.Cryptography.Ciphers.Asymmetric.RSA import RSA
from src.Cryptography.Ciphers.Cipher import Cipher
from src.Cryptography.Ciphers.Symmetric.AES import AES


class CypherTests(unittest.TestCase):

    def test_keys(self, cipher: AsymmetricCipher, sk, pk):
        pass

    @staticmethod
    def create_random_string(n=32):
        return ''.join(choices(string.ascii_uppercase + string.digits, k=n))

    def _test_single_cipher(self, text, crypto_scheme: Cipher):
        encrypted_text = crypto_scheme.encrypt(text)
        self.assertNotEqual(text, encrypted_text)
        decrypted_text = crypto_scheme.decrypt(encrypted_text)
        self.assertEqual(text, decrypted_text)

    def test_cipher(self, cipher: Cipher, iterations=100):
        for i in range(iterations):
            self._test_single_cipher(self.create_random_string(), cipher)

    def test_RSA(self):
        self.test_cipher(RSA(1024))

    def test_diffie_hellman(self):
        self.test_cipher(DiffieHellman())

    def test_elgamal(self):
        self.test_cipher(Elgamal())

    def test_goldwasser(self):
        self.test_cipher(Goldwasser())

    def test_aes(self):
        self.test_cipher(AES())


if __name__ == '__main__':
    unittest.main()
