from abc import ABC, abstractmethod


class IntegrationAlgorithm(ABC):

    def __init__(self, deg):
        self.degree = deg

    @abstractmethod
    def approximate_integral(self, fun, start, end):
        pass

    @abstractmethod
    def calculate_weights(self, *args, **kwargs):
        pass

    @abstractmethod
    def calculate_single_weight(self, *args, **kwargs):
        pass

    @abstractmethod
    def calculate_integration_points(self, start, end):
        pass

    @abstractmethod
    def error_magnitude(self):
        pass

    def integrate_polynomial(self, fun, start, end):
        anti_derivative = fun.get_anti_derivative()
        return anti_derivative(end) - anti_derivative(start)
