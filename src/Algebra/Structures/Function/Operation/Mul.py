from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import ComputationalGraphPart


class Mul(ComputationalGraphPart):
    _sign = "*"

    def get_anti_derivative(self, variable):
        pass

    def get_derivative(self, variable):
        first_derivative, second_derivative = self.derive_ops(variable)
        return self.left_op * second_derivative + first_derivative * self.right_op

    def evaluate(self, *args, **kwargs) -> float:
        left, right = self._get_values(*args, **kwargs)
        return left * right
