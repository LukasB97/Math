from src.Algebra.Structures.Function.Operator.ComputationalGraphPart import ComputationalGraphPart


class Pow(ComputationalGraphPart):
    def get_derivative(self, variable):
        pass

    def get_anti_derivative(self, variable):
        pass

    _sign = "^"

    def evaluate(self, *args, **kwargs) -> float:
        pass
