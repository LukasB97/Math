from abc import abstractmethod

from src.Cryptography.Ciphers.Cipher import Cipher


class AsymmetricCipher(Cipher):

    def __init__(self, sk=None, pk=None, *args, **kwargs):
        super().__init__(sk, *args, **kwargs)
        if pk is None:
            pk = self.public_key
        self.pk = pk

    @property
    @abstractmethod
    def public_key(self):
        pass
