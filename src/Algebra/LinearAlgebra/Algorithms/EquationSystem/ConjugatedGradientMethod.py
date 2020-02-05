from src.Algebra.Structures.Function.Norm import Norm
from Core.Factories.MatrixFactory import MatrixFactory


class ConjugatedGradientMethod:

    def calc_distance(self, r, direction, matrix_vector_product):
        return (r.transpose() * r) / (direction.transpose() * matrix_vector_product)

    def calculate_new_direction(self, r_new, r_old, d_i):
        gamma = (r_new.transpose() * r_new) / (r_old.transpose() * r_old)
        return r_new + gamma * d_i

    def solve(self, matrix, b, tolerance=0.01):
        x_i = MatrixFactory.create_random(matrix.row_count, 1)
        r_i = b - matrix * x_i
        direction_i = r_i
        for i in range(100):
            z_i = matrix * direction_i
            distance_i = self.calc_distance(r_i, direction_i, z_i)
            x_i += distance_i * direction_i
            r_i_new = r_i - distance_i * z_i
            direction_i = self.calculate_new_direction(r_i_new, r_i, direction_i)
            r_i = r_i_new
            n = Norm.euclidean_norm(r_i)
            if n < tolerance:
                break
        return x_i
