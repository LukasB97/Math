from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_instance(self, *args, **kwargs):
        pass
