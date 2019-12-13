import numpy

from src.kryptodat.FinitePolynomialField import FinitePolynomialField


class FinitePolynomialFieldFactory:

    def __init__(self, bits, generator):
        self.bits = bits
        self.generator = generator

    def xor(self, first_op: numpy.array, second_op: numpy.array):
        result_length = len(first_op)
        if len(second_op) > len(first_op):
            result_length = len(second_op)
        first_op = numpy.concatenate((numpy.zeros((result_length - len(first_op))), first_op))
        second_op = numpy.concatenate((numpy.zeros((result_length - len(second_op))), second_op))
        xor_result = numpy.zeros(result_length)
        for i in range(result_length):
            xor_result[i] = 1 if first_op[i] != second_op[i] else 0
        first_index = numpy.where(xor_result == 1)[0][-1] + 1
        return xor_result[:first_index]

    def create(self, value=None, bits=None) -> FinitePolynomialField:
        if value is not None:
            bit_string = "{0:b}".format(value)
            bits = numpy.zeros((len(bit_string)))
            for i in range(len(bit_string) - 1, -1, -1):
                bits[len(bits) - i - 1] = bit_string[i]
        else:
            assert bits is not None
        # self.xor(bits, self.generator)
        while len(bits) > self.bits:
            bits = self.xor(bits, self.generator)
        return FinitePolynomialField(numpy.concatenate((bits, numpy.zeros((self.bits - len(bits))))), self)


fact = FinitePolynomialFieldFactory(8, numpy.array([1, 1, 0, 1, 1, 0, 0, 0, 1]))
c = fact.create(123)
c2 = fact.create(45)
res = c + c2

res1 = c * c2

x = 10
