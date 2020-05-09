from abc import ABC

from src.Cryptography.Ciphers.Cipher import Cipher


class AsymmetricCipher(Cipher, ABC):

    def __init__(self, secret_key=None, pk=None, *args, **kwargs):
        super().__init__(secret_key, *args, **kwargs)
        if pk is None:
            pk = self.public_key
        self.public_key = pk


