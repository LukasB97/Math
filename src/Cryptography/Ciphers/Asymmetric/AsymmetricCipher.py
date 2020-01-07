from abc import ABC, abstractmethod

from src.Cryptography.Ciphers.Cipher import Cipher


class AsymmetricCipher(Cipher, ABC):

    def __init__(self, sk=None, pk=None, *args, **kwargs):
        self.pk = pk
        super().__init__(sk, *args, **kwargs)

    @abstractmethod
    def get_public_key(self):
        pass
