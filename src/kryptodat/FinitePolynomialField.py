import numpy


class FinitePolynomialField:

    @property
    def value(self):
        return int("".join(str(x) for x in self.bits)[::-1], 2)

    @property
    def order(self):
        s = numpy.where(self.bits == 1)[0][-1]
        return s

    def __init__(self, bits: numpy.array, factory):
        self.bits = numpy.array(bits, dtype=int)
        self.factory = factory

    def __add__(self, other):
        bits = self.bits+other.bits
        for i in range(len(bits)):
            bits[i] = bits[i] % 2
        return self.factory.create(bits=bits)

    def __mul__(self, other):
        if not isinstance(other, FinitePolynomialField):
            other = self.factory.create(value=other)
        bits = numpy.zeros((self.order + other.order + 1))
        for i in range(len(self.bits)):
            if self.bits[i] == 1:
                for j in range(len(other.bits)):
                    if other.bits[j] == 1:
                        bits[i + j] += 1
        for i in range(len(bits)):
            bits[i] = bits[i] % 2
        return self.factory.create(bits=bits)

    def __eq__(self, other):
        return (self.bits==other.bits).all()
