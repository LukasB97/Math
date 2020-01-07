import random


def AKS(n: int) -> bool:
    pass


def MillerRabinTest(n, s=50):
    if n < 2:
        return False
    for j in range(1, s + 1):
        a = random.randint(1, n - 1)
        i = n - 1
        b = []
        while i > 0:
            b.append(i % 2)
            i = i // 2
        d = 1
        for i in range(len(b) - 1, -1, -1):
            x = d
            d = (d * d) % n
            if d == 1 and x != 1 and x != n - 1:
                return False
            if b[i] == 1:
                d = (d * a) % n
        if d != 1:
            return False
    return True
