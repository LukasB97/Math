import random
from typing import Callable

from src.NumberTheory import PrimeNumberTests
from src.Tools.NumberGenerator.AbstractNumberGenerator import AbstractNumberGenerator, NumberGenerator, \
    SecureNumberGenerator

prime_summand = [1, 7, 11, 13, 17, 19, 23, 29]


class PrimeGenerator(AbstractNumberGenerator):

    def generate_random_integer(self, from_inclusive, to_inclusive) -> int:
        return self.random_generator.generate_random_integer(from_inclusive, to_inclusive)

    def __init__(self, random_generator: AbstractNumberGenerator,
                 prime_test: Callable[[int], bool] = PrimeNumberTests.miller_rabin_test):
        self.random_generator: AbstractNumberGenerator = random_generator
        self.prime_test: Callable[[int], bool] = prime_test

    @classmethod
    def std_insecure(cls):
        return PrimeGenerator(NumberGenerator(), PrimeNumberTests.miller_rabin_test)

    @classmethod
    def std_secure(cls):
        return PrimeGenerator(SecureNumberGenerator(), PrimeNumberTests.miller_rabin_test)

    def _get_from_to(self, from_incl, to_incl, bits):
        if not (from_incl is None or to_incl is None):
            if bits is None:
                raise ValueError("Missing parameters")
            return from_incl, to_incl
        if bits is None:
            raise ValueError("Missing parameters")
        return 2 ** bits, 2 ** (bits + 1) - 1

    def generate_prime(self, from_inclusive=None, to_inclusive=None, bits=None):
        from_inclusive, to_inclusive = self._get_from_to(from_inclusive, to_inclusive, bits)
        return self._generate_prime(from_inclusive, to_inclusive)

    def _generate_prime(self, from_inclusive=None, to_inclusive=None) -> int:
        n = self.random_generator.generate_random_integer(from_inclusive, to_inclusive)
        while not self.prime_test(n):
            n = self.random_generator.generate_random_integer(from_inclusive, to_inclusive)
        return n

    def generate_prime_theory(self, from_inclusive, to_inclusive) -> int:
        from_factor = from_inclusive // 30
        to_factor = to_inclusive // 30
        n = 30 * self.random_generator.generate_random_integer(from_factor, to_factor)
        n += random.choice(prime_summand)
        while not self.prime_test(n):
            n = 30 * self.random_generator.generate_random_integer(from_factor, to_factor)
            n += random.choice(prime_summand)
        return n

    def get_next_prime(self, lower_bound):
        while not self.prime_test(lower_bound + 1):
            lower_bound += 1
        return lower_bound + 1

    def generate_safe_prime(self, from_inclusive=None, to_inclusive=None, bits=None) -> int:
        from_inclusive, to_inclusive = self._get_from_to(from_inclusive, to_inclusive, bits)
        prime = self._generate_prime(from_inclusive, to_inclusive)
        while not self.prime_test((prime - 1) // 2):
            prime = self._generate_prime(from_inclusive, to_inclusive)
        return prime

    def generate_sophie_germain_prime(self, from_inclusive=None, to_inclusive=None, bits=None):
        from_inclusive, to_inclusive = self._get_from_to(from_inclusive, to_inclusive, bits)
        prime = self._generate_prime(from_inclusive, to_inclusive)
        while not self.prime_test(2 * prime + 1):
            prime = self._generate_prime(from_inclusive, to_inclusive)
        return prime
