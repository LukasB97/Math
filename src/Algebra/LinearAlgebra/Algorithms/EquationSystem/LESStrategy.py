from abc import ABC, abstractmethod

from src.Algebra.LinearAlgebra.Algorithms.EquationSystem.IterativeAlgorithm import IterativeAlgorithm


class LESStrategy(IterativeAlgorithm, ABC):

    def get_result(self, x, **kwargs):
        return x

    def execute(self, matrix, b):
        return self.run(self.create_state(matrix, b))

