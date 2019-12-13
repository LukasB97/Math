from dataclasses import dataclass
from typing import Dict, Any

from src.AlgebraicStructures.Function.Evaluable import Evaluable


@dataclass
class Variable(Evaluable):

    def evaluate(self, variables: Dict[str, float]) -> float:
        return variables[self.name]

    name: str
    value: float

