from src.Algebra.Structures.Function.Operator.ComputationalGraphPart import ComputationalGraphPart


class Div(ComputationalGraphPart):
    def get_anti_derivative(self, variable):
        pass

    _sign = "/"

    def get_derivative(self, variable, first_op, second_op):
        first_derivative = self.derive_op(variable, first_op)
        second_derivative = self.derive_op(variable, second_op)
        return (first_derivative * second_op - first_op * second_derivative) / (second_op * second_op)

    def evaluate(self, *args, **kwargs) -> float:
        pass
