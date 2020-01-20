from src.Algebra.LinearAlgebra.Decomposition import QRDecomposition
from src.Algebra.LinearAlgebra.Algorithms.EigenvalueAlgorithm import EigenvalueStrategy
from src.Algebra.Structures.Matrix.MatrixProperties.Triangular import Triangular, TriangularProperty


class QRAlgorithm(EigenvalueStrategy):

    def evaluate(self, matrix, digits=5):
        temp = matrix
        i = 0
        while True:
            if i == 100:
                break
            Q, R = temp.decompose(QRDecomposition())
            temp = R * Q
            a = temp.evaluate_property(Triangular())
            if a == TriangularProperty.UPPER_TRIANGULAR:
                print("Number of Factorizations: " + str(i + 1))
                break
            else:
                i += 1
            print(temp)
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
