from abc import ABC, abstractmethod


class Evaluable(ABC):

    @abstractmethod
    def evaluate(self, *args, **kwargs) -> float:
        pass

    def __call__(self, *args, **kwargs):
        return self.evaluate(*args, **kwargs)
