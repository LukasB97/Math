from abc import ABC, abstractmethod


class UniquelyIdentifiable(ABC):

    @abstractmethod
    def id(self):
        pass
