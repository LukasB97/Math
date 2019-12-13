from abc import ABC, abstractmethod
from typing import Dict, Any

from src.AlgebraicStructures.Function import Variable


class Evaluable(ABC):

    @abstractmethod
    def evaluate(self, variables: Dict[str, float]) -> float:
        pass