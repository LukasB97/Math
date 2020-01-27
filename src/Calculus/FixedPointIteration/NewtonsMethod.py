from src.Algebra.Structures.Function.Derivative import DifferentialQuotient
from src.Calculus.FixedPointIteration.FixedPointIteration import FixedPointIteration


class NewtonsMethod(FixedPointIteration):

    def __init__(self, function_to_evaluate, derivative=None):
        self.derivative = derivative
        super().__init__(function_to_evaluate)

    def evaluate_derivative(self, value):
        if self.derivative is None:
            return DifferentialQuotient.differential_quotient(self.function_to_evaluate, value)
        return self.derivative(value)

    def calc_next_step(self, value):
        val = value - self.function_to_evaluate(value) / self.evaluate_derivative(value)
        print(val)
        return val
