from abc import ABC, abstractmethod
from typing import Set


class Evaluable(ABC):

    @abstractmethod
    def get_variable_context(self) -> Set[str]:
        pass

    @abstractmethod
    def evaluate(self, *args, **kwargs) -> float:
        pass
