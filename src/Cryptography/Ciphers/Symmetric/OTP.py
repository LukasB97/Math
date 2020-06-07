from src.Cryptography.Ciphers.Cipher import Cipher


class OTP(Cipher):

    def encrypt_bytes(self, bytes_to_encrypt: bytes, *args, **kwargs):
        return bytes(a ^ b for a, b in zip(bytes_to_encrypt, self.secret_key))

    def decrypt_bytes(self, bytes_to_decrypt: bytes, *args, **kwargs):
        return bytes(a ^ b for a, b in zip(bytes_to_decrypt, self.secret_key))

    def create_key(self, length, *args, **kwargs):
        if not isinstance(length, int):
            raise ValueError("Length parameter required")
