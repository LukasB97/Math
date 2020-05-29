class MatrixNorm:

    @staticmethod
    def column_sum(matrix):
        sums = []
        for i in range(matrix.column_count):
            sums.append(matrix.get_column_vector(i).sum())
        return max(sums)
