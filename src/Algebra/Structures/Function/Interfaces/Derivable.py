from abc import ABC, abstractmethod


class Derivable(ABC):

    @abstractmethod
    def get_derivative(self, variable):
        pass
