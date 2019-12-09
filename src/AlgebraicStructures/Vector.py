from enum import Enum

from numpy import array

from src.AlgebraicStructures.Matrix.Matrix import Matrix


class Vector:

    def __getitem__(self, item: int):
        return self.values[item]

    def __setitem__(self, key, value):
        raise PermissionError("const")

    def __init__(self, values):
        self.values = array(values)

    def __len__(self):
        return len(self.values)

    def transpose(self):
        return Matrix(self.values.transpose())

    @classmethod
    def is_vector(cls, obj) -> bool:
        return False



