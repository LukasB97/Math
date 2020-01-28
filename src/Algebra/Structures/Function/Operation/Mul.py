from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import ComputationalGraphPart


class Mul(ComputationalGraphPart):
    _sign = "*"

    def get_anti_derivative(self, variable):
        pass

    def get_derivative(self, variable):
        first_derivative = self.derive_op(variable, first_op)
        second_derivative = self.derive_op(variable, second_op)
        return first_op * second_derivative + first_derivative * second_op

    def evaluate(self, *args, **kwargs) -> float:
        left, right = self._get_values(*args, **kwargs)
        return left * right
