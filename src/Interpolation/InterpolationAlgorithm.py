from abc import ABC, abstractmethod
from typing import Tuple, Set

from src.AlgebraicStructures.Function.AbstractFunction import AbstractFunction


class InterpolationAlgorithm(ABC):

    @abstractmethod
    def create_polynomial(self, data_points: Set[Tuple]) -> AbstractFunction:
        pass