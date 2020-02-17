from Algebra.Structures.Function.Interfaces.Evaluable import Evaluable


class Variable(Evaluable):

    def __len__(self) -> int:
        return 1

    def get_derivative(self, variable):
        if self.name == variable:
            return 1
        return

    def get_variable_context(self):
        return self.name.lower()

    def __init__(self, name):
        self.name: str = name
        self.value = ""

    def evaluate(self, *args, **kwargs) -> float:
        self.value = kwargs[self.name]
        return kwargs[self.name]

    def __repr__(self):
        return self.name
