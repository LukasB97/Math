from src.Calculus.Integration.QuadratureAlgorithm import QuadratureAlgorithm


class GaussQuadrature(QuadratureAlgorithm):

    def __init__(self, degree, weight_function):
        self.weight_function = weight_function
        super().__init__(degree)

    def calculate_single_weight(self, index):
        polynomial = self.create_lagrange_polynomial(index)
        polynomial_integral = self.integrate_polynomial(polynomial, 0, self.degree)
        return polynomial_integral / self.degree

    def calculate_integration_points(self, start, end):
        pass

    def error_magnitude(self):
        pass
