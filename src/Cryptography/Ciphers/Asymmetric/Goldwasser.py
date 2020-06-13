from src.Cryptography.Ciphers.Asymmetric.AsymmetricCipher import AsymmetricCipher
from src.Cryptography.Constants import MOD, PUB, P, Q
from src.NumberTheory.EuclideanAlgorithm import gcd
from src.NumberTheory.utils import is_quadratic_residue


class Goldwasser(AsymmetricCipher):

    def encrypt_bytes(self, bytes_to_encrypt: bytes, public_key=None, *args, **kwargs) -> bytes:
        bits = list(bin(int.from_bytes(bytes_to_encrypt, byteorder="big")).lstrip('0b'))
        length = public_key[MOD].bit_length()
        message_bits = 0
        for bit in bits:
            message_bits = message_bits << length
            message_bits += self.encrypt_bit(int(bit), public_key)
        return message_bits.to_bytes(length=(message_bits.bit_length() + 7) // 8, byteorder="big")

    def decrypt_bytes(self, bytes_to_decrypt: bytes, *args, **kwargs) -> bytes:
        message_bits = 0
        length = self.secret_key[P] * self.secret_key[Q]
        bits = list(bin(int.from_bytes(bytes_to_decrypt, byteorder="big")).lstrip('0b'))
        for bit in bits:
            message_bits = message_bits << length
            message_bits += self.decrypt_bit(int(bit))
        return message_bits.to_bytes(length=(message_bits.bit_length() + 7) // 8, byteorder="big")

    def create_key(self, key_length=256, *args, **kwargs):
        min_bits = (key_length + 2) // 2
        p = self.rng.generate_safe_prime(bits=min_bits)
        while p % 4 != 3:
            p = self.rng.generate_safe_prime(bits=min_bits)
        q = self.rng.generate_safe_prime(bits=min_bits)
        while q % 4 != 3 or p == q:
            q = self.rng.generate_safe_prime(bits=min_bits)
        mod = p*q
        return {P: p, Q: q}, {MOD: mod, PUB: mod - 1}

    def encrypt_bit(self, bit, encrypt_for):  # encryption for Goldwasser-Micali-Cryptosystem
        # call: GMEncrypt(pk,b) mit public key pk und Klartextbit b
        # return: Chiffretext c = (r*r*((n-1)**b)) % pk
        #          fuer random r aus {1,...,pk-1} mit ggT(r,pk)=1
        random_element = self.rng.generate_random_integer(0, encrypt_for[MOD] - 1)
        while gcd(random_element, encrypt_for[MOD]) != 1:
            random_element = self.rng.generate_random_integer(0, encrypt_for[MOD] - 1)
        return (encrypt_for[PUB] ** bit * random_element ** 2) % encrypt_for[MOD]

    def decrypt_bit(self, c):
        if is_quadratic_residue(c, self.secret_key[P], self.secret_key[Q]):
            return 0
        return 1
