import unittest
from time import time

from src.NumberTheory.utils import primitive_root_mod, group_mod_has_generator
from src.Tools.NumberGenerator.PrimeGenerator import PrimeGenerator


class MultiplicativeGroupTest(unittest.TestCase):

    def test_primitive_root(self):
        self.assertEqual(primitive_root_mod(3), 2)
        self.assertEqual(primitive_root_mod(5), 2)
        self.assertEqual(primitive_root_mod(23), 10)
        self.assertEqual(primitive_root_mod(31), 17)
        self.assertEqual(primitive_root_mod(49), 10)
        self.assertEqual(primitive_root_mod(71), 62)
        self.assertEqual(primitive_root_mod(42), None)

    def multiplicative_group_mod(self):
        pass

    def test_has_generator(self):
        self.assertEqual(group_mod_has_generator(), )


if __name__ == '__main__':
    unittest.main()
