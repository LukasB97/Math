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

    def encrypt_bit(self, b: bool):  # encryption for Goldwasser-Micali-Cryptosystem
        # call: GMEncrypt(pk,b) mit public key pk und Klartextbit b
        # return: Chiffretext c = (r*r*((n-1)**b)) % pk
        #          fuer random r aus {1,...,pk-1} mit ggT(r,pk)=1
        y = random_mul_group(self.public_key)
        b = 1 if b else 0
        return ((-1) ** b * y ** 2) % self.public_key

    @staticmethod
    def decrypt_bit(c):  # decryption for Goldwasser-Micali-Cryptosystem
        # call: GMDecrypt(sk,c) mit secure key sk und chiffriertes Bit c
        # return: dechiffriertes Bit
        #     0 falls c quadratic Rest mod pk ist
        #     1 falls c no quadratic Rest mod pk ist
        # IsQuadraticResidue
        pass

    # @property
    # def public_key(self):
    #     pass
