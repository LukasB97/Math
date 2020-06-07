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

    @staticmethod
    def create_random_string(n=32):
        return ''.join(choices(string.ascii_uppercase + string.digits, k=n))

    def _test_single_cipher(self, text, crypto_scheme: Cipher):
        encrypted_text = crypto_scheme.encrypt(text)
        self.assertNotEqual(text, encrypted_text)
        decrypted_text = crypto_scheme.decrypt(encrypted_text)
        self.assertEqual(text, decrypted_text)

    def _test_single_asymmetric_cipher(self, text, cipher_1: AsymmetricCipher, ciper_2: AsymmetricCipher):
        encrypted_text = cipher_1.encrypt(text, ciper_2.public_key)
        self.assertNotEqual(text, encrypted_text)
        decrypted_text = ciper_2.decrypt(encrypted_text)
        self.assertEqual(text, decrypted_text)

    def _test_cipher(self, cipher: Cipher, iterations=100):
        for i in range(iterations):
            self._test_single_cipher(self.create_random_string(), cipher)

    def test_asymmetric_cipher(self, cipher_1, cipher_2, iterations=100):
        for i in range(iterations):
            self._test_single_asymmetric_cipher(self.create_random_string(), cipher_1, cipher_2)

    def test_RSA(self):
        self.test_asymmetric_cipher(RSA(), RSA())

    def test_diffie_hellman(self):
        diffie = DiffieHellman()

    def test_elgamal(self):
        self.test_asymmetric_cipher(Elgamal(), Elgamal())

    def test_goldwasser(self):
        self.test_asymmetric_cipher(Goldwasser(), Goldwasser(), iterations=1)

    def test_aes(self):
        self._test_cipher(AES())


if __name__ == '__main__':
    unittest.main()
