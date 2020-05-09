from abc import abstractmethod
from datetime import datetime

from src.Core.Strategy import Strategy


class IterativeAlgorithm(Strategy):

    def __init__(self, iterations=None):
        self.iterations = iterations

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def run(self, state):
        t_start = datetime.now()
        iterations = 0
        while not self.check_break_condition(**state):
            state = self.next_iteration(**state)
            iterations += 1
        print("time: ", datetime.now() - t_start)
        print(iterations, " iterations")
        return self.get_result(**state)

    @abstractmethod
    def get_result(self, state):
        pass

    @abstractmethod
    def next_iteration(self, state, *args):
        pass

    @abstractmethod
    def check_break_condition(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_state(self, *args, **kwargs):
        pass
