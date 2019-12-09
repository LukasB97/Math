from src.AlgebraicStructures.Matrix.Matrix import Matrix


class BlockMatrix(Matrix):

    def __init__(self, matricies: list, fill=None):
        for i in range(len(matricies)):
            for j in range(len(matricies[0])):
                pass