import unittest
from time import time

from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class PrimeGeneratorTests(unittest.TestCase):

    @staticmethod
    def test_performance():
        # 13.12.19: std 5x faster
        from_ = 2 ** 24
        to = 2 ** 32
        p = PrimeGenerator.std_insecure()
        time1 = time()
        for i in range(1000):
            p._generate_prime(from_, to)
        time2 = time()
        print("normal", time2 - time1)
        time1 = time()
        for i in range(1000):
            p.generate_prime_theory(from_, to)
        time2 = time()
        print("theory", time2 - time1)


if __name__ == '__main__':
    unittest.main()
