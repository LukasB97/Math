from abc import ABC, abstractmethod
from typing import Tuple, List

from src.Algebra.Structures.Function.Function import Function


class InterpolationAlgorithm(ABC):

    @abstractmethod
    def create_polynomial(self, data_points: List[Tuple]) -> Function:
        pass
