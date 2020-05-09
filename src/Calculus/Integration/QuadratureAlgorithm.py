from src.Algebra.Structures.Function.Polynomial.Polynomial import Polynomial
from src.Calculus.Integration.IntegrationAlgorithm import IntegrationAlgorithm


class QuadratureAlgorithm(IntegrationAlgorithm):

    def __init__(self, degree):
        super().__init__(degree)
        self.weights = self.calculate_weights()

    def approximate_integral(self, fun, start, end):
        integration_points = self.calculate_integration_points(start, end)
        weighted_sum = 0
        for i in range(self.degree):
            weighted_sum += self.weights[i] * fun(integration_points[i])
        return (end - start) * weighted_sum

    def calculate_weights(self):
        weights = []
        for i in range(self.degree):
            weights.append(self.calculate_single_weight(i))
        return weights

    def create_lagrange_polynomial(self, index):
        denominator = Polynomial([1])
        numerator = Polynomial([1])
        for j in range(self.degree):
            if j == index:
                continue
            numerator *= Polynomial([-j, 1])
            denominator *= Polynomial([index - j])
        return numerator / denominator

    def calculate_single_weight(self, index):
        polynomial = self.create_lagrange_polynomial(index)
        polynomial_integral = self.integrate_polynomial(polynomial, 0, self.degree)
        return polynomial_integral / self.degree

    def calculate_integration_points(self, start, end):
        integration_points = []
        distance = (end - start) / self.degree
        for i in range(self.degree):
            integration_points.append(start + i * distance)
        return integration_points

    def error_magnitude(self):
        pass
