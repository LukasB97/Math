from src.Algebra.Structures.Function.Operation.ComputationalGraphPart import ComputationalGraphPart


class Add(ComputationalGraphPart):

    def get_anti_derivative(self, variable):
        pass

    _sign = "+"

    def get_derivative(self, variable):
        first_derivative, second_derivative = self.derive_ops(variable)
        return first_derivative + second_derivative

    def evaluate(self, *args, **kwargs) -> float:
        left, right = self._get_values(*args, **kwargs)
        return left + right
