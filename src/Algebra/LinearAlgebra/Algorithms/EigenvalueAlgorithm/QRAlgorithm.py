import numpy

from src.Algebra.LinearAlgebra.Decomposition.QRDecomposition import QRDecomposition
from src.Algebra.Structures.Function.MatrixNorm import MatrixNorm
from src.Algebra.Structures.Matrix.MatrixProperties.Eigenvalues import Eigenvalues
from src.Algebra.Structures.Matrix.MatrixProperties.Triangular import Triangular, TriangularProperty


class QRAlgorithm(Eigenvalues):

    def check_for_convergene(self, new_sum, last_sum, quotient):
        return new_sum <= abs(quotient * last_sum)

    def check_break(self, matrix, old_sums, quotient=0.5):
        new_sums = []
        convergence = False
        for i in range(matrix.column_count - 1):
            new_sums.append(matrix.get_column_vector(i, i + 1).sum())
            if self.check_for_convergene(new_sums[i], old_sums[i], quotient):
                convergence = True
        return convergence, new_sums

    def _evaluate(self, matrix, digits=5):
        temp = matrix
        qr_decomposition = QRDecomposition()
        last_lower_column_sum = numpy.full((matrix.column_count, 1), MatrixNorm.column_sum(matrix))
        i = 0
        while True:
            Q, R = qr_decomposition.decompose(temp)
            temp = R * Q
            a = Triangular().evaluate(temp.sub_matrix(0, temp.row_count - 1, 0, temp.column_count - 1))
            if a == TriangularProperty.UPPER_TRIANGULAR:
                print("Number of Factorizations: " + str(i + 1))
                break
            else:
                i += 1
            print(temp)
            convergence, new_sums = self.check_break(temp, last_lower_column_sum)
            if not convergence:
                break
            last_lower_column_sum = new_sums

        eigenvalues = set()
        for j in range(temp.column_count):
            only_zeros = True
            for i in range(j + 1, temp.row_count):
                if round(temp[i, j], digits) != 0:
                    only_zeros = False
                    break
            if only_zeros:
                eigenvalues.add(round(temp[j, j], digits))
        return eigenvalues
