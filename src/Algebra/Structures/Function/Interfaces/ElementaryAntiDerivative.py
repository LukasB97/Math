from abc import ABC, abstractmethod


class ElementaryAntiDerivative(ABC):

    @abstractmethod
    def get_anti_derivative(self, variable):
        pass
