from abc import ABC, abstractmethod
from collections import Sized


class Evaluable(ABC, Sized):

    @abstractmethod
    def evaluate(self, *args, **kwargs) -> float:
        pass

    def __call__(self, *args, **kwargs):
        return self.evaluate(*args, **kwargs)
