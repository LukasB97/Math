from abc import ABC, abstractmethod

from src.Cryptography.Ciphers.Cipher import Cipher


class AsymmetricCipher(Cipher, ABC):

    def __init__(self, secret_key=None, *args, **kwargs):
        super().__init__(secret_key, *args, **kwargs)
        self.public_key = self.get_public_key()

    @abstractmethod
    def get_public_key(self):
        pass
