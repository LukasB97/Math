from abc import ABC, abstractmethod


class CryptographicScheme(ABC):

    def __init__(self, secret_key, *args, **kwargs):
        if secret_key is None:
            secret_key = self.create_key(*args, **kwargs)
        self.secret_key = secret_key

    @abstractmethod
    def create_key(self, *args, **kwargs):
        pass
