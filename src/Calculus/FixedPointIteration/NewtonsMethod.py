from src.Algebra.Structures.Function.Derivative import DifferentialQuotient
from src.Calculus.FixedPointIteration.FixedPointIteration import FixedPointIteration


class NewtonsMethod(FixedPointIteration):

    def __init__(self, function_to_evaluate):
        super().__init__(function_to_evaluate)

    def calc_next_step(self, value):
        return value - self.call_function(value) / DifferentialQuotient.differential_quotient(self.function_to_evaluate,
                                                                                              value)
