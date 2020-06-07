import hashlib
from abc import abstractmethod

from src.Cryptography.CryptographicScheme import CryptographicScheme


class SignatureAlgorithm(CryptographicScheme):

    @abstractmethod
    def create_signature(self, message):
        pass

    @abstractmethod
    def verify_signature(self, message, signature, *args, **kwargs) -> bool:
        pass

    @staticmethod
    def hash(message):
        h = hashlib.sha256(bytearray(message, 'UTF8'))
        return h.hexdigest()
