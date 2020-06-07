from abc import ABC, abstractmethod


class CryptographicScheme(ABC):

    def __init__(self, secret_key, rng: type = None, has_public_key=False, *args, **kwargs):
        if rng is not None:
            self.rng = rng()
        if secret_key is None:
            if has_public_key:
                self.secret_key, self.public_key = self.create_key(*args, **kwargs)
            else:
                self.secret_key = self.create_key(*args, **kwargs)

    @abstractmethod
    def create_key(self, *args, **kwargs):
        pass
