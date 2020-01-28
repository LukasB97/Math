from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import ComputationalGraphPart


class Sub(ComputationalGraphPart):
    def get_anti_derivative(self, variable):
        pass

    _sign = "-"

    def get_derivative(self, variable, first_op, second_op):
        first_derivative = self.derive_op(variable, first_op)
        second_derivative = self.derive_op(variable, second_op)
        return first_derivative - second_derivative

    def evaluate(self, *args, **kwargs) -> float:
        left, right = self._get_values(*args, **kwargs)
        return left - right
