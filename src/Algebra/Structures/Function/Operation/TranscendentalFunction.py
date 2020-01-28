from typing import Set

from src.Algebra.Structures.Function import TranscendentalFunctionMapping
from src.Algebra.Structures.Function.AbstractFunction import AbstractFunction
from src.Algebra.Structures.Function.Evaluable import Evaluable
from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import ComputationalGraphPart
from src.Algebra.Structures.Function.Parser.ParseException import ParseException


class TranscendentalFunction(ComputationalGraphPart):

    def __init__(self, representation, function, params):
        super().__init__(function, params)
        self.representation = representation

    def evaluate(self, *args, **kwargs) -> float:
        params = None
        if isinstance(self.right_op, Evaluable):
            params = self.right_op.evaluate(*args, **kwargs)
        else:
            params = self.right_op
        return self.left_op(params)

    def get_derivative(self, variable):
        pass

    def get_anti_derivative(self, variable):
        pass

    @classmethod
    def from_string(cls, expression, parameter):
        if expression not in TranscendentalFunctionMapping.mappings:
            raise ParseException("could not find ", expression)
        return TranscendentalFunction(expression, TranscendentalFunctionMapping.mappings[expression], parameter)
