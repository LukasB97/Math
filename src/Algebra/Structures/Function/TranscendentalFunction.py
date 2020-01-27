from typing import Set

from src.Algebra.Structures.Function import TranscendentalFunctionMapping
from src.Algebra.Structures.Function.AbstractFunction import AbstractFunction
from src.Algebra.Structures.Function.Parser.ParseException import ParseException


class TranscendentalFunction(AbstractFunction):

    def __init__(self, operation, parameters):
        super().__init__(operation)

    def get_variable_context(self) -> Set[str]:
        pass

    def get_derivative(self, variable):
        pass

    def get_anti_derivative(self, variable):
        pass

    def evaluate(self, *args, **kwargs) -> float:
        pass

    @classmethod
    def from_string(cls, expression, parameter):
        if expression not in TranscendentalFunctionMapping.mappings:
            raise ParseException("could not find ", expression)
        return TranscendentalFunction(TranscendentalFunctionMapping.mappings[expression], parameter)
