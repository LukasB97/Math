from typing import Callable

from src.NumberTheory import PrimeNumberTests
from src.NumberTheory.AbstractNumberGenerator import AbstractNumberGenerator, NumberGenerator, SecureNumberGenerator


class PrimeGenerator:

    def __init__(self, random_generator: AbstractNumberGenerator,
                 prime_test: Callable[[int], bool] = PrimeNumberTests.MillerRabinTest):
        self.random_generator: AbstractNumberGenerator = random_generator
        self.prime_test: Callable[[int], bool] = prime_test

    @classmethod
    def std_insecure(cls):
        return PrimeGenerator(NumberGenerator(), PrimeNumberTests.MillerRabinTest)

    @classmethod
    def std_secure(cls):
        return PrimeGenerator(SecureNumberGenerator(), PrimeNumberTests.MillerRabinTest)

    def generate_prime(self, from_inclusive, to_inclusive) -> int:
        n = self.random_generator.generate_random_integer(from_inclusive, to_inclusive)
        while not self.prime_test(n):
            n = self.random_generator.generate_random_integer(from_inclusive, to_inclusive)
        return n

    def generate_safe_prime(self, from_inclusive, to_inclusive) -> int:
        prime = self.generate_prime(from_inclusive, to_inclusive)
        while not self.prime_test((prime - 1) // 2):
            prime = self.generate_prime(from_inclusive, to_inclusive)
        return prime

    def generate_sophie_germain_prime(self, from_inclusive, to_inclusive):
        prime = self.generate_prime(from_inclusive, to_inclusive)
        while not self.prime_test(2 * prime + 1):
            prime = self.generate_prime(from_inclusive, to_inclusive)
        return prime
