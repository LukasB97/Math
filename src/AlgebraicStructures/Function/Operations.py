from typing import List, Dict

from src.AlgebraicStructures.Function.ComputationalGraphPart import ComputationalGraphPart
from src.AlgebraicStructures.Function.Variable import Variable


class Operations:

    @classmethod
    def multiply(cls, operands: List[ComputationalGraphPart], variables: Dict[str, float]):
        result = 1
        for operand in operands:
            result *= operand.evaluate(variables)
        return result

    @classmethod
    def add(cls, operands: List[ComputationalGraphPart], variables: Dict[str, float]):
        result = 0
        for operand in operands:
            result += operand.evaluate(variables)
        return result

    @classmethod
    def subtract(cls, operands: List[ComputationalGraphPart], variables: Dict[str, float]):
        result = 0
        for operand in operands:
            result -= operand.evaluate(variables)
        return result

    @classmethod
    def divide(cls, operands: List[ComputationalGraphPart], variables: Dict[str, float]):
        if len(operands) > 2:
            raise ValueError()
        return operands[0].evaluate(variables) / operands[1].evaluate(variables)
