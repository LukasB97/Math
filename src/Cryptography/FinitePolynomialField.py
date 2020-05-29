class FinitePolynomialField:

    @classmethod
    def constructor(cls, polynomial=0b100011011):
        def create(value):
            return cls(value=value, polynomial=polynomial)

        return create

    def __index__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value

    def __init__(self, value, polynomial=0b100011011):
        if isinstance(value, self.__class__):
            pass
            # print("Info: Passed FinitePolynomialField instance to constructor instead of value")
        value = int(value)
        while len(bin(value)) >= len(bin(polynomial)):
            value = value ^ (polynomial << (len(bin(value)) - 11))
        self.value = value
        self.polynomial = polynomial

    def __int__(self):
        return self.value

    def __xor__(self, other):
        if self.polynomial != other.polynomial:
            raise ValueError("Different Polynomials")
        return self.__class__(self.value ^ other.value, self.polynomial)

    def __add__(self, other):
        if self.polynomial != other.polynomial:
            raise ValueError("Different Polynomials")
        return self.__class__(value=(self ^ other), polynomial=self.polynomial)

    def __mul__(self, other):
        if self.polynomial != other.polynomial:
            raise ValueError("Different Polynomials")
        result = 0
        self_value = self.value
        other_value = other.value
        while other_value > 0:
            if other_value & 1 == 1:
                result = result ^ self_value
            self_value = self_value << 1
            other_value = other_value >> 1
        while len(bin(result)) >= len(bin(self.polynomial)):
            result = result ^ (self.polynomial << (len(bin(result)) - 11))
        return self.__class__(value=result, polynomial=self.polynomial)

    def __rmul__(self, other):
        if type(other) != int:
            raise ValueError("unsupported types")
        return self * FinitePolynomialField(value=other, polynomial=self.polynomial)

    def __radd__(self, other):
        if type(other) != int:
            raise ValueError("unsupported types")
        return self + FinitePolynomialField(value=other, polynomial=self.polynomial)
