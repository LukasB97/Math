from abc import ABC, abstractmethod

from Cryptography.CryptographicScheme import CryptographicScheme


class HashFunction(CryptographicScheme, ABC):

    @abstractmethod
    def hash_value(self, value) -> str:
        pass
