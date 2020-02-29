from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def _evaluate(self, *args, **kwargs):
        pass
