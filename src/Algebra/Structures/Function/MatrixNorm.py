class MatrixNorm:

    @classmethod
    def column_sum(cls, matrix):
        sums = []
        for i in range(matrix.column_count):
            sums.append(matrix.get_column_vector(i).sum())
        return max(sums)
