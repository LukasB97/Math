class VectorNorm:

    @staticmethod
    def euclidean_norm(v):
        s = 0
        for i in range(v.row_count):
            s += v[i, 0] ** 2
        return s ** 0.5

    @staticmethod
    def maximum_norm(vector):
        return max(vector.matrix_vectors)

    @staticmethod
    def sum_norm(vector):
        return sum(vector.matrix_vectors)
