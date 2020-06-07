from abc import ABC, abstractmethod

from src.Cryptography.Ciphers.Cipher import Cipher


class AsymmetricCipher(Cipher, ABC):

    def __init__(self, secret_key=None, *args, **kwargs):
        super().__init__(secret_key, has_public_key=True, *args, **kwargs)

    @abstractmethod
    def create_public_key(self):
        pass

