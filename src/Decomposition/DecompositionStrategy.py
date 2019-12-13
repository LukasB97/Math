from abc import ABC, abstractmethod


class DecompositionStrategy(ABC):

    @abstractmethod
    def decompose(self, matrix):
        pass
