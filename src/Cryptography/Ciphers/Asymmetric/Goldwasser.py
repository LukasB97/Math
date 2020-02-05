from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.NumberTheory.utils import random_mul_group
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class Goldwasser(AsymmetricCipher):

    def get_public_key(self):
        pass

    def encrypt(self, message):
        message_bits = self.str2int(message)
        encrypted_message = 0
        for i in range(message_bits.bit_length()):
            bit_i = (message_bits % 2) == 1
            message_bits = message_bits >> 1
            encrypted_message += self.encrypt_bit(bit_i) * 2 ** i
        return encrypted_message

    def decrypt(self, chiffretext):
        decrypted_bits = 0
        for i in range(chiffretext.bit_length()):
            bit_i = (chiffretext % 2) == 1
            chiffretext = chiffretext >> 1
            decrypted_bits += self.decrypt_bit(bit_i) * 2 ** i
        return self.int2str(decrypted_bits)

    def create_key(self, bits=1024, *args, **kwargs):
        prime_generator = PrimeGenerator.std_insecure()
        p = prime_generator.generate_safe_prime(2 ** (bits / 2), 2 ** ((bits / 2) + 1) - 1)
        while p % 4 != 3:
            p = prime_generator.generate_safe_prime(2 ** (bits / 2), 2 ** ((bits / 2) + 1) - 1)
        q = prime_generator.generate_safe_prime(2 ** (bits / 2), 2 ** ((bits / 2) + 1) - 1)
        while q % 4 != 3 or p == q:
            q = prime_generator.generate_safe_prime(2 ** (bits / 2), 2 ** ((bits / 2) + 1) - 1)
        return p, q

    def encrypt_bit(self, b: bool):  # Verschluesselung fuer Goldwasser-Micali-Kryptosystem
        # Aufruf: GMEncrypt(pk,b) mit public key pk und Klartextbit b
        # Ausgabe: Chiffretext c = (r*r*((n-1)**b)) % pk
        #          fuer Zufallszahl r aus {1,...,pk-1} mit ggT(r,pk)=1
        y = random_mul_group(self.pk)
        b = 1 if b else 0
        return ((-1) ** b * y ** 2) % self.pk

    def decrypt_bit(self, c):  # Entschluesselung fuer Goldwasser-Micali-Kryptosystem
        # Aufruf: GMDecrypt(sk,c) mit secure key sk und chiffriertes Bit c
        # Ausgabe: dechiffriertes Bit
        #     0 falls c quadratischer Rest mod pk ist
        #     1 falls c kein quadratischer Rest mod pk ist
        IsQuadraticResidue
        return ...
