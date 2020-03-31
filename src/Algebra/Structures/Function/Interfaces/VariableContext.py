from abc import ABC, abstractmethod
from typing import Set


class VariableContext(ABC):

    @abstractmethod
    def get_variable_context(self) -> Set[str]:
        pass
