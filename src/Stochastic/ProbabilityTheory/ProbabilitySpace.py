from src.Stochastic.ProbabilityTheory.Event import Event


class ProbabilitySpace:

    def __init__(self, sample_space, event_set, probability_measure):
        self.sample_space = sample_space
        self.probability_measure = probability_measure
        self.event_set = event_set

    @staticmethod
    def get_probability(event: Event):
        if event is None:
            return 0
        pass
