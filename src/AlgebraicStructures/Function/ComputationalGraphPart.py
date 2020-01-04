from dataclasses import dataclass
from typing import Callable, List, Dict

from src.AlgebraicStructures.Function.Variable import Variable


@dataclass
class ComputationalGraphPart:
    operation: Callable[[List['ComputationalGraphPart']], float]
    operands: List['ComputationalGraphPart']

    @property
    def completely_evaluable(self):
        for operand in self.operands:
            if not isinstance(operand, Variable):
                return False
        return True

    def evaluate(self, variables: Dict[str, float]) -> float:
        return self.operation(self.operands, variables)
