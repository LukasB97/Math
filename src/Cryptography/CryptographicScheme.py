from abc import ABC, abstractmethod


class CryptographicScheme(ABC):

    def __init__(self, sk, *args, **kwargs):
        if sk is None:
            sk = self.create_key(*args, **kwargs)
        self.sk = sk

    @abstractmethod
    def create_key(self, *args, **kwargs):
        pass
