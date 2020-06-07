from abc import ABC, abstractmethod

from src.Cryptography.Ciphers.Cipher import Cipher
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class AsymmetricCipher(Cipher, ABC):

    def __init__(self, secret_key=None, rng=PrimeGenerator.std_insecure, *args, **kwargs):
        super().__init__(secret_key, rng=rng, has_public_key=True, *args, **kwargs)

    @abstractmethod
    def encrypt_bytes(self, bytes_to_encrypt: bytes, public_key=None, *args, **kwargs) -> bytes:
        pass

    def encrypt(self, message: str, public_key=None, *args, **kwargs) -> str:
        return super().encrypt(message, public_key=public_key, *args, **kwargs)



