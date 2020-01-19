from abc import ABC, abstractmethod
from typing import Set

from src.Core.Strategy import Strategy


class EigenvalueStrategy(Strategy, ABC):

    @abstractmethod
    def execute(self, matrix, *args, **kwargs) -> Set[float]:
        pass