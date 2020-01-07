from abc import ABC, abstractmethod


class DecompositionStrategy(ABC):

    @abstractmethod
    def solve(self, matrix, target_vector):
        pass

    @abstractmethod
    def decompose(self, matrix):
        pass
