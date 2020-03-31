from abc import abstractmethod
from collections import Sized, Callable


class Evaluable(Sized, Callable):

    @abstractmethod
    def evaluate(self, *args, **kwargs) -> float:
        pass

    def __call__(self, *args, **kwargs):
        return self.evaluate(*args, **kwargs)
