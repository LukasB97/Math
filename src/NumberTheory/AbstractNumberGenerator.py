import random
import secrets
from abc import ABC, abstractmethod


class AbstractNumberGenerator(ABC):

    @abstractmethod
    def generate_random_integer(self, from_inclusive, to_inclusive) -> int:
        pass


class NumberGenerator(AbstractNumberGenerator):

    def generate_random_integer(self, from_inclusive, to_inclusive) -> int:
        return random.randint(from_inclusive, to_inclusive)


class SecureNumberGenerator(NumberGenerator):

    def __init__(self):
        self.generator = secrets.SystemRandom()

    def generate_random_integer(self, from_inclusive, to_inclusive) -> int:
        return self.generator.randint(from_inclusive, to_inclusive)
