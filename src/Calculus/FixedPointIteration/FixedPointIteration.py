from abc import ABC, abstractmethod
from typing import Callable


class FixedPointIteration(ABC):

    def __init__(self, function_to_evaluate: Callable):
        self.function_to_evaluate = function_to_evaluate

    @abstractmethod
    def calc_next_step(self, value):
        pass

    def iterate(self, start_value, number_of_iterations: int):
        for i in range(number_of_iterations):
            new_value = self.calc_next_step(start_value)
            if new_value == start_value:
                return new_value
            start_value = new_value
        return start_value
