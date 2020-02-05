import string
import unittest
from random import random

from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Ciphers.Cipher import Cipher


class CypherTests(unittest.TestCase):

    def test_keys(self, cipher: AsymmetricCipher, sk, pk):
        pass

    def create_random_string(self, n=32):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

    def test_single_cipher(self, text, crypto_scheme: Cipher):
        encrypted_text = crypto_scheme.encrypt(text)
        self.assertNotEqual(text, encrypted_text)
        decrypted_text = crypto_scheme.decrypt(encrypted_text)
        self.assertEqual(text, decrypted_text)

    def test_cipher(self, cipher: Cipher, iterations=100):
        for i in range(iterations):
            self.test_single_cipher(self.create_random_string(), cipher)


if __name__ == '__main__':
    unittest.main()
